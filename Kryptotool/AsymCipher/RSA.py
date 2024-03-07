# RSA
from Crypto.Util.number import getPrime, inverse, GCD, bytes_to_long
from hashlib import sha1
import json
import os
import sys


def generate_keypair(name: str, keysize = 1024):
	private_path = f"./keys/{name}_PRIVATE.key"
	public_path = f"./keys/{name}_PUBLIC.key"
	if os.path.exists(private_path) or os.path.exists(public_path):
		sys.exit(f"WARNING: The file {public_path} or {private_path} already exists!")

	# Number Magic
	# private
	private_key = {
		"Name": name,
		"key": {
			"N": N,
			"d": d,
			"e": e,
		}
	}
	with open(private_path, "w") as file:
		file.write(json.dumps(private_key))
	# public
	public_key = {
		"name": name,
		"key": {
			"N": N,
			"e": e,
		}
	}
	with open(public_path, "w") as file:
		file.write(json.dumps(public_key))

def read_privatekey(filename: str):
	assert(filename.endswith("_PRIVATE.key"))
	with open(filename, "r") as file:
		private_key = json.loads(file.readline())
		return private_key
	return -1

def read_publickey(filename: str):
	assert(filename.endswith("_PUBLIC.key"))
	with open(filename, "r") as file:
		public_key = json.loads(file.readline())
		return public_key
	return -1


def encrypt(m: int, pubkey):
	return 0

def decrypt(ct: int, privkey):
	return 0

def hash_message(m: str):
	return 0

def sign(m: str, privkey):
	return 0

def verify_signature(m: str, sgn: int, pubkey):
	return 0
