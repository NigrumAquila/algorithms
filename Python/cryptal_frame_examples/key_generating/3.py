import random
import string
from os import urandom


nbytes = 16
generated = urandom(nbytes)

# def randomString(stringLength=8):
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for i in range(stringLength))

# rs = randomString(nbytes * 2)

# print("Random String is ", rs)


# i = {'a': 's', 'b': rs}
i = {'b': generated}

print(generated)

for value in i.values():
    for c in value:
        # print(hex(ord(c))[2:], end='')
        print(chr(c), end='')
    print()


# g = random.randint(2**128, 2**156)
g = 20081880401709194526581280298337345170368957921
i = hex(g)
b = g.to_bytes(20, byteorder='big')
print(g, i, b)
f = open('file', 'wb')
for c in {13}:
    print(c)
    f.write(c.to_bytes(1, byteorder='big'))
f.close()

fr = open('file', 'rb')

for c in fr.read(1):
    print(c)

fr.close()