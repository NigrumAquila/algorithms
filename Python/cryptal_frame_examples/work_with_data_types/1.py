def enc():
    fileR = open('data/jpg.jpg', 'rb')
    dstFileEncryptW = open('data/jpg.encrypted.jpg', 'wb')
    while True:
        c = fileR.read(1)
        if not c: break
        integer = int.from_bytes(c, byteorder='big')+1000
        encryptedChar = integer.to_bytes(2, byteorder='big')
        dstFileEncryptW.write(encryptedChar)

def dec():
    dstFileEncryptR = open('data/jpg.encrypted.jpg', 'rb')
    dstFileDecryptW = open('data/jpg.decrypted.jpg', 'wb')
    while True:
        c = dstFileEncryptR.read(2)
        if not c: break
        integer = int.from_bytes(c, byteorder='big')-1000
        decryptedChar = integer.to_bytes(1, byteorder='big')
        dstFileDecryptW.write(decryptedChar)

enc()
dec()

print(open('data/jpg.jpg', 'rb').read(10))
print(open('data/jpg.decrypted.jpg', 'rb').read(10))

# file = open('data/jpg.jpg', 'rb')
# data = file.read()
# print(type(data), data)
# print(data)
# file.seek(0)

# f = open('data/text.encrypted.txt', 'rb')
# print(int.from_bytes(f.read(2), byteorder='big')-1000)
