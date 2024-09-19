import rsa
(pubkey, privkey) = rsa.newkeys(512)
(bob_pub, bob_priv) = rsa.newkeys(512)
message = 'Asymmetric Encryption'.encode('utf8')
crypto = rsa.encrypt(message, bob_pub)
print(crypto)
message = rsa.decrypt(crypto, bob_priv)
print(message.decode('utf8'))



##from sympy import randprime
##import random
##
##def gcd(a,b):
##    while(b!=0):
##        a,b=b,a%b
##    return a
##
##def getPublicExponent(num):
##    for i in range (2,num):
##        if (gcd(i,num)==1):
##            return i
##    return None
##
##def modularInverse(val,domain):
##    for i in range (domain):
##        if((val*i)%domain==1):
##            return i
##    return None
##
##def encrypt(msg,e,n):
##    var=[]
##    for char in msg:
##        if(char==' '):
##            i=0
##        else:
##            i=ord(char)-96
##            i=pow(i,e)%n
##        var.append(i)
##    return var
##
##def decrypt(arr,d,n):
##    var=''
##    for num in arr:
##        i=pow(num,d)%n
##        if(i==0):
##            var+=' '
##        else:
##            i=chr(i+96)
##            var+=i
##    return var
##
##
#### Key generation
##
###Prime number generation
##p=randprime(3,10)
##q=randprime(10,20)
##
##
###Modulus
##n=p*q
##
###Euler's Totient Function
##phi_n=(p-1)*(q-1)
##
###Public Exponent
##e=getPublicExponent(phi_n)
##
###Private Exponent
##d=modularInverse(e,phi_n)
##
##
##print(p,q,n,phi_n,e,d)
##
##plainText="Asymmetric Encryption"
##plainText=plainText.lower()
##
#### Encryption
##pt=encrypt(plainText,e,n)
##print(plainText,pt)
##
#### Decryption
##ct=decrypt(pt,d,n)
##print(ct)
