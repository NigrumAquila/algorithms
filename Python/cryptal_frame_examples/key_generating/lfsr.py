# print(type(random_key))
# print(random_key, int.from_bytes(random_key, byteorder='big'), type(int.from_bytes(random_key, byteorder='big')))


# print(s, type(s))
# print(bin(int(s)))
# exit()

# print(random_key)
# print(int.from_bytes(random_key, byteorder='big'))
# print(bin(int.from_bytes(random_key, byteorder='big')))
# print(bytes(random_key, "ascii"))
# print(int.from_bytes(bytes(random_key, "ascii"), byteorder="big"))
# exit()

# print(int.from_bytes(random_key, byteorder='big'))
# print(bin(int.from_bytes(random_key, byteorder='big')))
# exit()


def generateKey():
    from os import urandom

    random_key = urandom(1)
    s = str(int.from_bytes(random_key, byteorder='big'))
    # print(int(bin(int(s))[2:]))
    
    return int(bin(int(s))[2:])

generateKey()

def generateKey():
    from os import urandom

    random_key = bin(int.from_bytes(urandom(1), byteorder='big'))[2:]
    #path: start -> bytes -> int -> bin[2:] (str) -> int -> end
    # b = (i)[2:]
    # print(type(b), b)
    # print(type(int(b)), int(b))
    # end = int(b)

    # s = str(int.from_bytes(random_key, byteorder='big'))
    # print(int(bin(int(s))[2:]))
    
    # return int(bin(int(s))[2:])
    return random_key



h = bytes.fromhex("0F").hex()
ht = type(h)
b = b'\x0f'
bt = type(b)
b_h = b.hex()
b_ht = type(b_h)
print(h, ht, b, bt, b_h, b_ht)
print(binascii.unhexlify('0f'))
# print(binascii.hexlify(b).decode().unhexlify(), type(binascii.hexlify(b).decode()))
exit()
