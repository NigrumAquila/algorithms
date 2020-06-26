from random import randrange
from hashlib import sha1
from src.common.multiplicativeInverse import multiplicativeInverse
from sympy import isprime


def generate_p_q(L, N):
    g = N 
    n = (L - 1) // g
    b = (L - 1) % g
    while True:
        while True:
            s = randrange(1, 2 ** (g))
            a = sha1(bin(s).encode()).hexdigest()
            zz = (s + 1) % (2 ** g)
            z = sha1(bin(zz).encode()).hexdigest()
            U = int(a, 16) ^ int(z, 16)
            mask = 2 ** (N - 1) + 1
            q = U | mask
            if isprime(q):
                break
        i = 0 
        j = 2 
        while i < 4096:
            V = []
            for k in range(n + 1):
                arg = (s + j + k) % (2 ** g)
                zzv = sha1(bin(arg).encode()).hexdigest()
                V.append(int(zzv, 16))
            W = 0
            for qq in range(0, n):
                W += V[qq] * 2 ** (160 * qq)
            W += (V[n] % 2 ** b) * 2 ** (160 * n)
            X = W + 2 ** (L - 1)
            c = X % (2 * q)
            p = X - c + 1  # p = X - (c - 1)
            if p >= 2 ** (L - 1):
                if isprime(p):
                    return p, q
            i += 1
            j += n + 1


def generate_g(p, q):
    while True:
        h = randrange(2, p - 1)
        exp = (p - 1) // q
        g = pow(h, exp, p)
        if g > 1:
            break
    return g


def generate_keys(g, p, q):
    x = randrange(2, q)
    y = pow(g, x, p)
    return x, y


def generate_params(L, N):
    p, q = generate_p_q(L, N)
    g = generate_g(p, q)
    return p, q, g


def sign(M, p, q, g, x):
    if not validate_params(p, q, g):
        raise Exception("Invalid params")
    while True:
        k = randrange(2, q)
        r = pow(g, k, p) % q
        m = int(sha1(M).hexdigest(), 16)
        try:
            s = (multiplicativeInverse(k, q) * (m + x * r)) % q
            return r, s
        except ZeroDivisionError:
            pass


def verify(M, r, s, p, q, g, y):
    if not validate_params(p, q, g):
        raise Exception("Invalid params")
    if not validate_sign(r, s, q):
        return False
    try:
        w = multiplicativeInverse(s, q)
    except ZeroDivisionError:
        return False
    m = int(sha1(M).hexdigest(), 16)
    u1 = (m * w) % q
    u2 = (r * w) % q
    v = (pow(g, u1, p) * pow(y, u2, p)) % p % q
    if v == r:
        return True
    return False


def validate_params(p, q, g):
    if isprime(p) and isprime(q):
        return True
    if pow(g, q, p) == 1 and g > 1 and (p - 1) % q:
        return True
    return False


def validate_sign(r, s, q):
    if r < 0 and r > q:
        return False
    if s < 0 and s > q:
        return False
    return True


if __name__ == "__main__":
    N = 160
    L = 1024
    p, q, g = generate_params(L, N)
    x, y = generate_keys(g, p, q)

    text = open('tasks', 'r').read()
    M = text.encode()
    r, s = sign(M, p, q, g, x)
    if verify(M, r, s, p, q, g, y):
        print('All ok')
        print(M)
        print(r)
        print(s)
        print(p)
        print(q)
        print(g)
        print(y)
        print(x)