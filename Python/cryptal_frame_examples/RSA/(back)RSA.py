from ..common.primeGenerator import primeGenerator
from ..common.checkPrimesRelatively import checkPrimesRelatively
from ..common.multiplicativeInverse import multiplicativeInverse


class RSA:
    @staticmethod
    def generateKeys():
        p = primeGenerator(2**10, 2**20); q = primeGenerator(2**10, 2**20)
        n = p*q; fi = (p-1)*(q-1)
        e = primeGenerator(1, fi)
        while(checkPrimesRelatively(e, fi) != True):
            e = primeGenerator(1, fi)
        d = multiplicativeInverse(e, fi)
        publicKey = {'e': e, 'n': n}; privateKey = {'d': d, 'n': n}
        print('p:', p, 'q:', q, '\nn:', n, 'fi:', fi, '\ne:', e, 'd:', d, '\npublic key:', publicKey, 'private key:', privateKey)
        return publicKey, privateKey

    encrypt = staticmethod(lambda publicKey, message: pow(message, int(publicKey['e']), int(publicKey['n'])))
    decrypt = staticmethod(lambda privateKey, cipher: pow(cipher, int(privateKey['d']), int(privateKey['n'])))