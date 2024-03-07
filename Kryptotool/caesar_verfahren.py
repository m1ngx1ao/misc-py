al = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
	"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def encrypt_with_key(message : str, key : int) -> str:
	result = ''
	letters = list(message)
	for l in letters:
		if l not in al:
			result += l
		else:
			result += al[(al.index(l) + key) % len(al)]
	return result

def decrypt_with_key(message : str, key : int) -> str:
	result = ''
	letters = list(message)
	for l in letters:
		if l not in al:
			result += l
		else:
			result += al[(al.index(l) - key) % len(al)]
	return result

def encrypt_without_key(message : str):
	letters = list(message)
	for key, _ in enumerate(al):
		result = ''
		for l in letters:
			if l not in al:
				result += l
			else:
				result += al[(al.index(l) + key) % len(al)]
		print(result)

def decrypt_without_key(message : str):
	letters = list(message)
	for key, _ in enumerate(al):
		result = ''
		for l in letters:
			if l not in al:
				result += l
			else:
				result += al[(al.index(l) - key) % len(al)]
		print(result)

#print(decrypt_with_key("KDOOR", 3))
#print(encrypt_with_key("EXIIL", 3))
#print(encrypt_without_key("TYU RKHW BYURUDPUBB YIJ UYDU IFEHDRKHW RUY 450 C Ü. DD QKV UYDUC QRVQBBUDTUD RUHWIFEHD QC XQDW TUI ISXBEIIRUHWI ÜRUH TUH IJQTJ RQT BYURUDPUBB YC BQDTAHUYI SQBM YD RQTUD-MÜHJJUCRUHW. TYU RKHW BYURUDPUBB MQH UYDIJ TYU RUTUKJUDTIJU RKHW TUI MÜHJJUCRUHWYISXUD ISXMQHPMQBTUI."))
#print(decrypt_without_key("NSO LEBQ VSOLOXJOVV SCD OSXO CZYBXLEBQ LOS 450 W Ü. XX KEP OSXOW KLPKVVOXNOX LOBQCZYBX KW RKXQ NOC CMRVYCCLOBQC ÜLOB NOB CDKND LKN VSOLOXJOVV SW VKXNUBOSC MKVG SX LKNOX-GÜBDDOWLOBQ. NSO LEBQ VSOLOXJOVV GKB OSXCD NSO LONOEDOXNCDO LEBQ NOC GÜBDDOWLOBQSCMROX CMRGKBJGKVNOC."))