from hashlib import sha256
from random import randint
from sympy import randprime, mod_inverse
from math import gcd


def findPrimitiveRoot(p):
    if p == 2:
            return 1
    p1 = 2
    p2 = (p-1) // p1

    while(1):
        g = randint( 2, p-1 )
        if not (pow( g, (p-1)//p1, p ) == 1):
            if not pow( g, (p-1)//p2, p ) == 1:
                return g


plain_text = 'text'
hash = sha256(plain_text.encode())
digest = int.from_bytes(hash.digest(), byteorder='big')

p = randprime(2**127, 2**128); g = findPrimitiveRoot(p)
x = randint(1, p-1); y = pow(g, x, p)

k = randprime(1,p-1)
while(gcd(k,p) != 1):
	k = randprime(1, p-1)
r = pow(g,k,p); s = mod_inverse(k, p-1) * (digest - x * r) % (p-1)


assert 0 < r and r < p
assert 0 < s and s < p-1

u1, u2 = pow(y, r, p), pow(r, s, p)
lhs, rhs = u1 * u2 % p, pow(g, digest, p)
print('ok') if(lhs == rhs) else print('no ok')

