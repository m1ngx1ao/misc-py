# Diffie Hellmann
from Crypto.Random.random import getrandbits
from Crypto.Util.number import long_to_bytes

P1 = 179769313486231590770839156793787453197860296048756011706444423684197180216158519368947833795864925541502180565485980503646440548199239100050792877003355816639229553136239076508735759914822574862575007425302077447712589550957937778424442426617334727629299387668709205606050270810842907692932019128194467627007
g1 = 2

def initialisiere(p = P1, g = g1):
	a = getrandbits(256)
	A = pow(g, a, p)
	return (a, {"p": p, "g": g, "A": A})

def finalisiere(a, return_msg, p = P1):
	shared_key = pow(return_msg, a, p)
	return shared_key

def empfange(init_msg):
	p = init_msg.get("p")
	g = init_msg.get("g")
	A = init_msg.get("A")
	b = getrandbits(256)
	B = pow(g, b, p)
	shared_key = pow(A, b, p)
	return (shared_key, {"B": B})
