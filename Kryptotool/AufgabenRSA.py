from hashlib import sha256
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse
# Im Folgenden sind ein paar einführende Aufgaben zum Thema RSA gegeben

# 1)
p = 18973
g = 229
e = 23
#print(pow(g, e, p))
# TODO: Berechne g^e mod p: 3125


# 2)
p = 17
q = 29
e = 65537 # 0x10001
m = 42
N = p * q
result = pow(m, e, N)
#print(result)
# TODO: Verschlüssle m mit Hilfe der beiden Primzahlen p, q und dem Exponenten e : 399
# TIPP: Caesarveschlüsselt^^ (Berechne N, und wende dann #1 an) 


# 3)
p = 1257309560244439029013084173949
# TODO: Berechne die Phifunktion von N
q = 6905732203350735796224475384109
phi = (p-1) * (q-1) # = 8682643119760774624038685012275259437017352868712713186818384


# 4)
p = 1257309560244439029013084173949
q = 6905732203350735796224475384109
# TODO: Berechne den privaten Schlüssel d zum öffentlichen Schlüssel e und den Primzahlen p und q
# TIPP: Implementiere den euklidischen Algorithmus oder finde eine passende Bibliothek
e = 65537 # 0x10001
phi = (p-1) * (q-1)
d = inverse(e, phi) # = 2561457223819442705359780521344124173448487119698667878510561

# 5)
c = 3291635183402273971613077055961803587619338801045127769806089
# TODO: Ich habe dir mit obigen öffentlichen Schlüssel e, sowie den Primzahlen aus #4) eine Nachricht verschlüsselt
# Hinweis: Zum Verschlüsseln muss der String erstmal in eine Zahl und die Zahl danach wieder in einen String umgewandelt werden. 
# Hier ein Beispiel:
	#s = "einString"
	#z = bytes_to_long(s.encode())
	#print(z)
	#s = long_to_bytes(z).decode()
	#print(s)
m = pow(c, d, p*q)
z = long_to_bytes(m).decode() # z = flag{feels_like_magic}

def wandele_nachricht_von_bytes_zu_zahl(m: bytes, d : int, N : int, signiere : bool) -> int:
	h = sha256(m)
	g = h.digest()
	m_long = bytes_to_long(g)
	if signiere:
		return pow(m_long, d, N)
	return m_long

# 6)
m = "DuVeränderstMeineNachrichtNichtOhneDassAlleEsMerken!".encode()
# = 7271500855470013249175728109189658261272753052063439216828517
# TODO: Signiere den Hashwert mit deinem privaten Schlüssel, um den Spruch wahr zu machen.
signiert_m = wandele_nachricht_von_bytes_zu_zahl(m, d, p*q, True)

m1 = "DochIchÄndereDeineNachrichtOhneDassIrgendwerEsMerkt!".encode()
m2 = "DuVeränderstMeineNachrichtNichtOhneDassAlleEsMerken!".encode()
# TODO: Schreibe ein assert, welches für die jeweiligen Nachrichten überprüft, ob du sie unterschrieben hast
m2 = wandele_nachricht_von_bytes_zu_zahl(m2, d, p*q, False)
assert m2 == wandele_nachricht_von_bytes_zu_zahl(m, d, p*q, False)
assert m2 != signiert_m

signiert_m1 = wandele_nachricht_von_bytes_zu_zahl(m1, d, p*q, True)
assert m1 != signiert_m1
