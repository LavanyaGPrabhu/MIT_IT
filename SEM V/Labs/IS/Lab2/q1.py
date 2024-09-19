from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad,unpad
import base64

key=b'A1B2C3D4'
message=b'Confidential Data'

paddedMessage=pad(message,DES.block_size)
des=DES.new(key,DES.MODE_ECB)

#Encryption
enc=des.encrypt(paddedMessage)
enc1=base64.b64encode(enc).decode('ascii')
print("Encryptd text: ",enc1)

#Decryption
dec=des.decrypt(enc)
dec1=unpad(dec,DES.block_size)
print("Decryptd text: ",dec1.decode())
