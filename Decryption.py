f = open("ToBeSent for Decryption/cipher2.txt",'r',encoding='utf-8')
cipher = f.read()
import base64
import numpy as np
import cv2
# reading P and R images
P = cv2.imread(r'C:\Users\varsh\Downloads\Novel-Image-Encryption-Algorithm-using-AES-and-Visual-Cryptography-main\Novel-Image-Encryption-Algorithm-using-AES-and-Visual-Cryptography-main\P.png')
R = cv2.imread(r'C:\Users\varsh\Downloads\Novel-Image-Encryption-Algorithm-using-AES-and-Visual-Cryptography-main\Novel-Image-Encryption-Algorithm-using-AES-and-Visual-Cryptography-main\R.png')
#intializing h and w
h = np.shape(P)[0] #rows
w = np.shape(P)[1] #coloumn
# initialize the image CK
CK = np.ones((h,w,1), dtype = 'uint8')
for i in range(h):
    for j in range(w):
        ck = P[i][j][0] ^ R[i][j][0] 
        CK[i][j][0] = ck
K1 = []
for i in range(len(CK)):
    K1.append(0)

for i in range(len(CK)):
    count = 0
    for j in range(len(CK[i])):
        if CK[i][j][0] == 0: #counting the number of pixels which have 0 as value
            count += 1
    K1[i] = chr(count)
K1 = "".join(K1) # list into string
K1
import hashlib 
SK1 = hashlib.sha256(K1.encode()) 

print("The hexadecimal equivalent of SHA256 is : ") 
print(SK1.hexdigest())
# AES 256 in OFB mode:
from Crypto.Cipher import AES
from Crypto.Random import new as Random
from hashlib import sha256
from base64 import b64encode,b64decode

class AESCipher:
    def __init__(self,data,key):
        self.block_size = 16
        self.data = data
        self.key = sha256(key.encode()).digest()[:32]
        self.pad = lambda s: s + (self.block_size - len(s) % self.block_size) * chr (self.block_size - len(s) % self.block_size)
        self.unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    def decrypt(self):
        cipher_text = b64decode(self.data.encode())
        iv = cipher_text[:self.block_size]
        cipher = AES.new(self.key,AES.MODE_OFB,iv)
        return self.unpad(cipher.decrypt(cipher_text[self.block_size:])).decode()
import pandas as pd
xdf = pd.DataFrame(columns = ['1','2'])
a = []
b = []
for i in P:
    k = 0
    n1 = []
    n2 = []
    for j in i:
        if k%2==0:
            n1.append(np.sum(j))
        else:
            n2.append(np.sum(j))
        k += 1    
    a.append(sum(n1))
    b.append(sum(n2))
xdf['1'] = a
xdf['2'] = b
ydf = pd.DataFrame(columns = ['1','2'])
a = []
b = []
for i in R:
    k = 0
    n1 = []
    n2 = []
    for j in i:
        if k%2==0:
            n1.append(np.sum(j))
        else:
            n2.append(np.sum(j))
        k += 1    
    a.append(sum(n1))
    b.append(sum(n2))
ydf['1'] = a
ydf['2'] = b
from sklearn.linear_model import LinearRegression
LRmodel = LinearRegression()
LRmodel.fit(xdf,ydf)
zdf = pd.DataFrame(columns = ['1','2'])
a = []
b = []
for i in CK:
    k = 0
    n1 = []
    n2 = []
    for j in i:
        if k%2==0:
            n1.append(np.sum(j))
        else:
            n2.append(np.sum(j))
        k += 1    
    a.append(sum(n1))
    b.append(sum(n2))
zdf['1'] = a
zdf['2'] = b
predict = LRmodel.predict([[sum(zdf['1']),sum(zdf['2'])]])
x = round(predict[0][0])%26
y = round(predict[0][1])%26
cipher = cipher.split(' ')
txt = []
for each in cipher:
    try:
        ch = ord(each) - x + y #ord means we are converting back to ascii format
        txt.append(int(ch))
    except:
        print(each)