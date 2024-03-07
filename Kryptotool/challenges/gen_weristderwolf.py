from random import shuffle
import json
from Crypto.Util.number import getPrime, bytes_to_long


namen = "Börner Adrian, Helmig Fabian, Imkamp Judith, Morin Mauricio, Obreiter Sophie, Püllen Anika, Walz Lukas, Wieben Marie-Christine,  Yu Hugo, Zheng Timo".split(", ")
namen = list(map(lambda x: " ".join(x.split(" ")[::-1]), namen))

def gen_key_and_stuff(m, e):
	p = getPrime(512)
	q = getPrime(512)
	N = p * q
	ct = pow(bytes_to_long(m.encode()), e, N)
	return {"N": N, "e": e, "ct": ct}

rollen = []		
with open("weristderwolf.in", 'r') as inputfile:
	alles = inputfile.readlines()
	shuffle(alles)

	outputfile = open("weristderwolf.out", "w")
	solutionfile = open("weristerwolf.sol", "w")

	i = 0
	for m, e in map(lambda x : x.strip().split(", "), alles):
		solutionfile.write(f"{namen[i]}: {m}\n")
		i += 1
		e = int(e)
		outputfile.write(json.dumps(gen_key_and_stuff(m, e)))
		outputfile.write("\n")

	outputfile.close()
	solutionfile.close()
