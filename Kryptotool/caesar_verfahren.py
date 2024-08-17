al = [chr(i + ord('A')) for i in range(26)]
def get_new_index(l: str, key : int, operator: str):
	if operator == '+':
		return al.index(l) + key
	if operator == '-':
		return al.index(l) - key
	assert False

def get_new_message(message : str, key : int, operator: str) -> str:
	result = ''
	letters = list(message)
	for l in letters:
		if l not in al:
			result += l
		else:
			result += al[get_new_index(l, key, operator) % len(al)]
	return result

def encrypt_with_key(message : str, key : int) -> str:
	return get_new_message(message, key, '+')

def decrypt_with_key(message : str, key : int) -> str:
	return get_new_message(message, key, '-')

def encrypt_without_key(message : str):
	for key, _ in enumerate(al):
		result = encrypt_with_key(message, key)
		print(result)

def decrypt_without_key(message : str):
	for key, _ in enumerate(al):
		result = decrypt_with_key(message, key)
		print(result)

#print(decrypt_with_key("KDOOR", 3))
#print(encrypt_with_key("EXIIL", 3))
#print(encrypt_without_key("TYU RKHW BYURUDPUBB YIJ UYDU IFEHDRKHW RUY 450 C Ü. DD QKV UYDUC QRVQBBUDTUD RUHWIFEHD QC XQDW TUI ISXBEIIRUHWI ÜRUH TUH IJQTJ RQT BYURUDPUBB YC BQDTAHUYI SQBM YD RQTUD-MÜHJJUCRUHW. TYU RKHW BYURUDPUBB MQH UYDIJ TYU RUTUKJUDTIJU RKHW TUI MÜHJJUCRUHWYISXUD ISXMQHPMQBTUI."))
#print(decrypt_without_key("NSO LEBQ VSOLOXJOVV SCD OSXO CZYBXLEBQ LOS 450 W Ü. XX KEP OSXOW KLPKVVOXNOX LOBQCZYBX KW RKXQ NOC CMRVYCCLOBQC ÜLOB NOB CDKND LKN VSOLOXJOVV SW VKXNUBOSC MKVG SX LKNOX-GÜBDDOWLOBQ. NSO LEBQ VSOLOXJOVV GKB OSXCD NSO LONOEDOXNCDO LEBQ NOC GÜBDDOWLOBQSCMROX CMRGKBJGKVNOC."))