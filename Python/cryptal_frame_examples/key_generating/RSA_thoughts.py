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