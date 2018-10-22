import pyAesCrypt
from os import stat, remove
from Crypto.Cipher import AES
# encryption/decryption buffer size - 64K
obj = AES.new('This is a key123', AES.MODE_CBC,'This is an IV456')
# encrypt

fOut = open("client_secret.aes", "wb")
with open("client_secret1.json", "rb") as fIn:
    message = fIn.read()
    fOut.write(obj.encrypt(message))
fOut.close()