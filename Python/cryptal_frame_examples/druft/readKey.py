def readKey(alg, key):
    key = {}

    if alg == 'rsa':
        modulusFile = open('keys/rsa.modulus', 'r')
        if key == 'public':
            pubkFile = open('keys/rsa.pk', 'r')
            key['e'] = pubkFile.read()
            pubkFile.close()
        elif key == 'private':
            pkFile = open('keys/rsa.pk', 'r')
            pkFile.close()
        key['n'] = modulusFile.read()
        modulusFile.close()
    
    return key