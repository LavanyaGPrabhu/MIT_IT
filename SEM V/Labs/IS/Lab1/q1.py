def inverseKeyDomain(key,domain):
	for i in range (domain):
		if((key*i)%domain==1):
			return i
	return None
	
		    
def additiveCipher(message,key,type):
	enc=[]
	if(type=="encrypt"):
		for char in message:
			if(char==' '):
				enc.append(' ')	
			elif(ord(char)>=97 and ord(char)<=122):
				enc.append(chr(((ord(char)-97+key)%26)+97))
			elif(ord(char)>=65 and ord(char)<=90):
				enc.append(chr(((ord(char)-65+key)%26)+65))
		return "".join(enc)
	elif(type=="decrypt"):
		for char in message:
			if(char==' '):
				enc.append(' ')	
			elif(ord(char)>=97 and ord(char)<=122):
				enc.append(chr(((ord(char)-97-key)%26)+97))
			elif(ord(char)>=65 and ord(char)<=90):
				enc.append(chr(((ord(char)-65-key)%26)+65))
		return "".join(enc)

def multiplicativeCipher(message,key):
	enc=[]
	for char in message:
		if(char==' '):
			enc.append(' ')	
		elif(ord(char)>=97 and ord(char)<=122):
			enc.append(chr((((ord(char)-97)*key)%26)+97))
		elif(ord(char)>=65 and ord(char)<=90):
			enc.append(chr((((ord(char)-65)*key)%26)+65))
	return "".join(enc)

def affineCipher(message,key1,key2,type):
	enc=[]
	if(type=="encrypt"):
		for char in message:
			if(char==' '):
				enc.append(' ')	
			elif(ord(char)>=97 and ord(char)<=122):
				enc.append(chr((((ord(char)-97)*key1+key2)%26)+97))
			elif(ord(char)>=65 and ord(char)<=90):
				enc.append(chr((((ord(char)-65)*key1+key2)%26)+65))
		return "".join(enc)
	elif(type=="decrypt"):
		for char in message:
			if(char==' '):
				enc.append(' ')	
			elif(ord(char)>=97 and ord(char)<=122):
				enc.append(chr((((ord(char)-97-key2)*key1)%26)+97))
			elif(ord(char)>=65 and ord(char)<=90):
				enc.append(chr((((ord(char)-65-key2)*key1)%26)+65))
		return "".join(enc)
	    

domain=26
message="I am learning information security"

key=20
print("\nAdditive cipher encryption with key = 20")
enc1a=additiveCipher(message,key,"encrypt")
print(enc1a)

print("\nAdditive cipher decryption with key = 20")
dec1a=additiveCipher(enc1a,key,"decrypt")
print(dec1a)

key=15
print("\nMultiplicative cipher encryption with key = 15")
enc1b=multiplicativeCipher(message,key)
print(enc1b)

print("\nMultiplicative cipher decryption with key = 15")
inverseKey=inverseKeyDomain(key,domain)
if(type(inverseKey)==None):
	print("Inverse doesn't exist")
else:
	dec1b=multiplicativeCipher(enc1b,inverseKey)
	print(dec1b)

key1=15
key2=20
print("\nAffine cipher encryption with keys = 15,20")
enc1c=affineCipher(message,key1,key2,"encrypt")
print(enc1c)

print("\nAffine cipher decryption with key = 15,20")
inverseKey1=inverseKeyDomain(key1,domain)
if(type(inverseKey1)==None):
	print("Inverse doesn't exist")
else:
	dec1c=affineCipher(enc1c,inverseKey1,key2,"decrypt")
	print(dec1c)
