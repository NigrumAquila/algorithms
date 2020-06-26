from sympy import randprime
import random
import math


def multiplicativeInverse(n, q):
    return egcd(n, q)[0] % q

def egcd(a, b):
    s0, s1, t0, t1 = 1, 0, 0, 1
    while b > 0:
        q, r = divmod(a, b)
        a, b = b, r
        s0, s1, t0, t1 = s1, s0 - q * s1, t1, t0 - q * t1
    return s0, t0, a


minrange, maxrange = 100, 10000
p, q = randprime(minrange, maxrange), randprime(minrange, maxrange)
n = p*q
pubkey = {'p': p, 'q': q}
privkey = {'n': n}
m = 86

c = pow(m, 2, n)


m1 = pow(c,((p+1)//4), p)
m2 = pow(-c,((p+1)//4), p)
m3 = pow(c,((q+1)//4), q)
m4 = pow(-c,((q+1)//4), q)

print(m1)
print(m2)
print(m3)
print(m4)
# exit()

a = q*multiplicativeInverse(q,p)
b = p*multiplicativeInverse(p,q)
print(a)
print(b)

M1 = (a*m4 + b*m3) % n
M2 = (a*m1 + b*m4) % n
M3 = (a*m2 + b*m3) % n
M4 = (a*m2 + b*m4) % n

print(M1)
print(M2)
print(M3)
print(M4)
