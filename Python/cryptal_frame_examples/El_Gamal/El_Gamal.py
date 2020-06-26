from sympy import randprime, primitive_root
import random


def multiplicativeInverse(n, q):
    return egcd(n, q)[0] % q

def egcd(a, b):
    s0, s1, t0, t1 = 1, 0, 0, 1
    while b > 0:
        q, r = divmod(a, b)
        a, b = b, r
        s0, s1, t0, t1 = s1, s0 - q * s1, t1, t0 - q * t1
    return s0, t0, a

m = 11
p = randprime(100, 1000)
g = primitive_root(p)
x = random.randint(1, p-1)
y = pow(g, x, p)

# encr
k = random.randint(1, p-1)
a = pow(g, k, p)
b = ((y ** k) * m) % p
#decr

dm = b*a**(p-1-x) % p



print(m, a, b, dm)
