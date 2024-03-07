# Aufgaben DiffieHellmann
from Crypto.Util.number import inverse

import caesar_verfahren as c

# 1)
p = 757
g = 187
d = inverse(g, p) # d = 336
print('Aufgabe 1: ' + str(d))
# TODO: Finde ein inverses d, sodass g * d == 1 mod p


# 2)
p = 24071
for g in range(2, p - 1):
	s = set()
	i = 0
	pw = pow(g, i, p)
	while pw not in s:
		s.add(pw)
		i += 1
		pw = pow(g, i, p)
	if len(s) == p - 1:
		print('Aufgabe 2: ' + str(g))
		break

# TODO: Finde eine primitivwurzel g, sodass g^i alle Elemente von {1, ... p-1} durchläuft. Überprüfe, ob dies auch tatsächlich der Fall ist


# 3)
p = 179769313486231590770839156793787453197860296048756011706444423684197180216158519368947833795864925541502180565485980503646440548199239100050792877003355816639229553136239076508735759914822574862575007425302077447712589550957937778424442426617334727629299387668709205606050270810842907692932019128194467627007
g = 2
a = 3692666510802673526214414656749903875429869235299630712139820877467528978804442807708418343602088817030762083678104822926107918287111947178729334261857953998772979041697002943143261806604174180163394732748718729459346689097681034114339361249383921296063826372954069432151417743787797047731632691183566
A = pow(g, a, p)
print('Aufgabe 3: ' + str(A))
# TODO: Berechne A = g^a mod p


# 4)
B = 95573141217605574027482545983199758392856093052420808837431832304005527617148262476360912761623046068276367229336389529219602213373194572523342209283918964590360943968494456644285756177218258294922714648182482183987531850193352557950677265484928408416884245635311241035702322347051945007252776972503164783881
# TODO: Du erhälst dies als Antwort auf deine Nachricht (p, g, A). Wie lautet euer gemeinsames Geheimnis secret?
secret = pow(B, a, p)
print('Aufgabe 4: ' + str(secret))


# 5)
# TODO: Überprüfe, Berechne die Antwort von deinem Gegenüber und verifiziere, dass sie gleich sind
#b = inverse(g, p)
#secret_other = pow(A, b, p)
#assert(secret == secret_other)

# 6)
ct = "YDAAPNJYZMCZGGHVII?"
# Nutze das zuvor generierte gemeinsame Geheimnis secret und berechne den Caesarschlüssel k = (secret % 26), um die Nachricht zu entschlüsseln.
k = (secret % 26)
print('Aufgabe 6: ' + c.decrypt_with_key(ct, k))