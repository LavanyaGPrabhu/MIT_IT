import numpy as np
def preprocess(msg):
  msg=msg.replace(' ','').lower()
  if len(msg)%2!=0:
    msg+='x'
  return msg

def textToNum(txt):
  return [ord(i)-ord('A') for i in txt]
          
def numToText(num):
  return ''.join(chr(i + ord('A')) for i in map(int,num))

def hillEncrypt(msg,key):
  msg=preprocess(msg)
  msgNum=textToNum(msg)
  CT=[]
  for i in range(0,len(msgNum),2):
    vector=np.array(msgNum[i:i+2]).reshape(2,1)
    encVector=np.dot(key,vector)%26
    CT.append(encVector)  
  return numToText(CT)

key=np.array([[3,3],[2,7]])
msg="We live in an insecure world"
ppm=preprocess(msg)
encMsg=hillEncrypt(ppm,key)
print(f"Encrypted message: {encMsg}")

# dec