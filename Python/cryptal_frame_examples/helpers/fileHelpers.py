def writeKeys(key, alg):
    pathToKeys = 'keys/'
    
    if alg == 'rsa':
        pkFile = open(pathToKeys + 'rsa.pk', 'w')
        pubkFile = open(pathToKeys + 'rsa.pubk', 'w')
        modulusFile = open(pathToKeys + 'rsa.modulus', 'w')

        for pubkChar in str(key[0]['e']):
            pubkFile.write(pubkChar)
        pubkFile.close()

        for pkChar in str(key[1]['d']):
            pkFile.write(pkChar)
        pkFile.close()

        for modulusChar in str(key[0]['n']):
            modulusFile.write(modulusChar)
        modulusFile.close()

    if alg == 'lrr':
        pkFile = open(pathToKeys + 'lrr.pk', 'w')
        
        for pkChar in str(key):
            pkFile.write(pkChar)
        pkFile.close()


def generateKeys():
    public_key = {'e': 234, 'n': 14}
    private_key = {'d': 432134, 'n': 232}
    return public_key, private_key
