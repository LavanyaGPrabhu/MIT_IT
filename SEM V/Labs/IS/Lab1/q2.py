def vigenereCipher(message,key,type):
	count=0
	enc=[]
	if(type=="encrypt"):
		for char in message:
			if(ord(char)>=97 and ord(char)<=122):
				enc.append(chr(((ord(char)-97+(ord(key[count])-97))%26)+97))
			elif(ord(char)>=65 and ord(char)<=90):
				enc.append(chr(((ord(char)-65+(ord(key[count])-65))%26)+65))
			count+=1
		return "".join(enc)
	elif(type=="decrypt"):
		for char in message:
			if(ord(char)>=97 and ord(char)<=122):
				enc.append(chr(((ord(char)-97-(ord(key[count])-97))%26)+97))
			elif(ord(char)>=65 and ord(char)<=90):
				enc.append(chr(((ord(char)-65-(ord(key[count])-65))%26)+65))
			count+=1
		return "".join(enc)

def autokeyCipher(message,key,type):
	if(type=="encrypt"):
		result=vigenereCipher(message,key,type)
		return result
	elif(type=="decrypt"):
		count=0
		enc=[]
		for char in message:
			# if(ord(char)>=97 and ord(char)<=122):
			dec=(chr(((ord(char)-97-(ord(key[count])-97))%26)+97))
			# elif(ord(char)>=65 and ord(char)<=90):
			# 	dec=(chr(((ord(char)-65-(ord(key[count])-65))%26)+65))
			enc.append(dec)
			key=key+dec
			count+=1
		return "".join(enc)

def getKey(message, key):
	msgLen=len(message)
	while len(key)<msgLen:
		key+=key
	key=key[:msgLen]
	return key

def getChar(key):
	keyStream=''
	for char in key:
		keyStream+=chr(ord(char)-48+97)
	return keyStream

domain=26
message="the house is being sold tonight"
message=message.replace(" ","")
key="dollars"
keyStream=getKey(message,key)

enc2a=vigenereCipher(message,keyStream,"encrypt")
print("\nVigenere cipher encryption with key = 'dollars':",enc2a)

dec2a=vigenereCipher(enc2a,keyStream,"decrypt")
print("\nVigenere cipher decryption with key = 'dollars':",dec2a)


key="7"
key=getChar(key)
keyStream=key+message
keyStream=keyStream[:len(message)]

enc2b=autokeyCipher(message,keyStream,"encrypt")
print("\nAutokey cipher encryption with key = 7:",enc2b)

dec2b=autokeyCipher(enc2b,key,"decrypt")
print("\nAutokey cipher decryption with key = 7:",dec2b)
