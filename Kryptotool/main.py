# Bibliotheken, die wir brauchen
# import pyperclip
from Crypto.Util.number import long_to_bytes, bytes_to_long

# symmetrische Verfahren
import Cipher.identityCipher
import Cipher.reverseCipher
# import Cipher.CaesarCipher as Caesar # (https://inventwithpython.com/cipherwheel/)
# import AffineCipher # 
# import Cipher.SubstitutionCipher as Substitution
# import Cipher.VigenereCipher as Vigenere # (https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Base.html)
# import TranspositionCipher # (Auch bekannt als Skytale)
# import DeinEigenesVerfahren oder in den Worten von Bruce Schneier: Jeder kann sich ein Verfahren ausdenken, was er selbst nicht knacken kann.

# asymmetrische Verfahren
import AsymCipher.RSA as RSA
import AsymCipher.DH as DH

if __name__ == "__main__":
	publicKey = 0 # Tuple
	privateKey = 0 # Tuple

	key = 0
	message = "Hallo welt!"
	cipher = Cipher.reverseCipher.encrypt(message)
	print(cipher)
