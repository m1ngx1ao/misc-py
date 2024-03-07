#!/usr/bin/env python3
# coding=utf-8
import json
import logging
import socket
import threading
import sys
from queue import Queue
import time

#Network
IP = "localhost"
PORT = 1893


""" wir brauchen Nachrichten an die Clients für:
- von wem kommt eine Nachricht
- an wen eine Nachricht gehen soll
- welche Clients sind connected? (am Anfang)
- welcher Client hat sich gerade disconnected?

Nachrichten sehen wie folgt aus
{"to": 1337, "message": "hallo"}  # gerichtete Nachricht
{"message": "hallo"}  # Broadcast-Nachricht
{"message": {"N": p, "e": e, "name": "Max Mustermann"}}  # Broadcast-Nachricht mit beliebigem Wert
# Bei den clients kommt dann die Nachricht X in der Form:
{"fromm": id, "message": X }

Daneben gibt es die Nachrichten vom Server
{"id": 42}  # Du hast dich erfolgreich angemeldet und deine ID ist 42
{"id": [42, 13, 6], "connected": True}  # Neue Clients namens 42, 13, 6
{"id": [42, 187], "connected": False}  # Clients namens 42, 187 sind verschwunden
"""


def dictFromJSON(jsonstr :str):  # senderid only for logging
    try:
        decode = json.JSONDecoder().decode(jsonstr)
        if type(decode) != dict:
            return None
    except json.JSONDecodeError:
        return None
    return decode

def dictToJSON(obj : dict):
    return json.dumps(obj)


class ServerThread:

    def __init__(self):
        self.lock = threading.RLock()    # lock for clients and currentId
        self.clients = dict()
        self.currentId = 0
        self.sendQueue :Queue = Queue()  # This should contain dicts

    def start(self, ip=IP, port=PORT):
        self.ip = ip
        self.port = port
        self.ListenThread = threading.Thread(daemon=True, target=self.__listen)
        self.ListenThread.start()
        threading.Thread(daemon=True, target=self.__sendWorker).start()
        
    def terminate(self):
        client_sockets = list(self.clients.keys())
        for cs in client_sockets:
            self.clients[cs].close()
        self.socket.close()

    def __listen(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.info("Binding to port " + str(self.port))
        self.socket.bind(('', self.port))
        self.socket.listen()
        logging.info("From now on listening to connections")
        while True:
            try:
                (client, addr) = self.socket.accept()
            except InterruptedError:
                logging.info("aborted accepting")
                return
            except OSError:
                logging.info("Closed the socket")
                return
            logging.info("new client: "+str(self.currentId))

            # Weise neuem Client seine ID zu
            self.sendQueue.put({"id": self.currentId})
            with self.lock:
                newID = self.currentId
                self.currentId += 1
                self.clients[newID] = client
            threading.Thread(daemon=True, target=(self.__listenClient), args=(client, newID)).start()

    def __listenClient(self, client, id):
        while True:
            data = ''
            while True:
                try:
                    data += client.recv(2048).decode("utf-8")
                except UnicodeDecodeError:
                    continue
                except OSError as e:
                    with self.lock:
                        self.clients.pop(id)
                    return
                if "\n" in data:
                    data = data.strip()
                    break
            
            logging.debug(f"Data from Client {id}: {data}")

            content = dictFromJSON(data)
            if content is None:
                logging.error(f"{id} sent no valid json: {data}")
            elif "message" in content.keys() and \
                 (("to" not in content.keys() and len(content) == 1) or \
                    ("to" in content.keys() and len(content) == 2)):
                content["fromm"] = id
                self.sendQueue.put(content)
            else:
                logging.error(f"Client {id} did not send message in a matching format: {data}")


    def __send(self, id :int, data :dict):
        with self.lock:
            if self.clients is None:
                logging.critical("Error: first call start()")
                return
            try:
                #logging.debug("sending: "+data)
                if id in self.clients:
                    self.clients[id].send((dictToJSON(data) + "\n").encode("utf-8"))
            except BaseException:
                logging.info("Tried to send to closed socket -> remove player")
    
                self.clients.pop(id)
                self.sendQueue.put({"id": id}) # disconnected event
                return

    def __sendWorker(self):
        while True:
            element = self.sendQueue.get()
            if "id" in element:
                greeting = element["id"] in self.clients.keys()
                
                # Liste andere Clients
                with self.lock:
                    clientCopies = self.clients.copy()  

                if greeting: # falls neuer Client
                    self.__send(element["id"], element)
                    self.__send(element["id"], {"id": list(clientCopies.keys()), "connected": True})

                # Informiere Rest über status von id
                for client in clientCopies:
                    self.__send(client, {"id": [element["id"]], "connected": greeting})
            elif "to" in element:
                logging.debug(f"sending({element['to']}): {element['message']}")
                self.__send(element["to"], element)
            else:
                with self.lock:
                    clientCopies = self.clients.copy()
                logging.debug(f"broadcasting to {len(clientCopies)} Clients: {element}")
                for client in clientCopies:
                    self.__send(client, element)

        

class ClientThread:

    def start(self, ip=IP, port=PORT):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))
        self.id = -1
        self.reachable_clients = set()
        self.received_messages = Queue()
        threading.Thread(target=self.__listenServer, daemon=True).start()
    
    def __send(self, data):
        self.socket.send((dictToJSON(data) + "\n").encode("utf-8"))

    def send(self, to :int, message):
        self.__send({"to": to, "message": message})

    def broadcast(self, message):
        self.__send({"message": message})
    
    def terminate(self):
        self.socket.close()
    
    def __listenServer(self):
        while True:
            data = ''
            while True:
                try:
                    data += self.socket.recv(2048).decode("utf-8")
                except UnicodeDecodeError:
                    continue
                except BaseException:
                    return
                if "\n" in data:
                    data = list(data.strip().split("\n"))
                    break
            logging.debug(f"Client {self.id} received: {data}")
            for d in data:
                content = dictFromJSON(d)
                
                if content is None:
                    logging.error(f"No valid json! {d} - {content}")
                elif "id" in content:
                    if type(content["id"]) == int: # setze ID
                        self.id = content["id"]
                    elif type(content["id"]) == list and "connected" in content: # Ändere Reachable clients
                        if content["connected"]:
                            self.reachable_clients |= set(content["id"])
                        else:
                            self.reachable_clients -= set(content["id"])
                    else:
                        logging.error(f"Client {id} received invalid server package: {content}")
                else:
                    self.received_messages.put(content)
                    print(f"Received Message: {content}") #
                    content["message"]


def localTest():
    server = ServerThread()
    server.start()

    client = ClientThread()
    client.start()
    time.sleep(1)
    client2 = ClientThread()
    client2.start()
    time.sleep(1)
    client2.broadcast('hallo')
    time.sleep(1)
    client.terminate()
    time.sleep(1)

    server.terminate()
    exit()   


def runServer():
    server = ServerThread()
    server.start()

    time.sleep(24 * 60)

    server.terminate()
    exit()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s %(message)s", stream=sys.stdout)
    
    runServer()

    