def readKey(alg, typeKey = None):
    pathToKey = pickFile()

    if alg == 'RSA':
        # fullKey = open(pathToKey, 'r').readlines()
        # if typeKey == 'public': key['e'] = fullKey[0].splitlines()[0][]
        # elif typeKey == 'private': key['d'] = fullKey[0].splitlines()[0]
        # key['n'] = fullKey[1].splitlines()[0]
        # return key
        keys = {}
        fileParams = open(pathToKey, 'rb').readlines()
        for line in fileParams:
            line = line.decode()
            trim = line.find(':')
            key = line[:trim]
            keys[key] = int(line[trim+2:], 16)
        return keys

    elif alg == 'LRR':
        return open(pathToKey, 'r').read()

    elif alg == 'EC':
        return readECparams(pathToKey)

    elif alg == 'EL_GAMAL':
        return int.from_bytes(open(pathToKey, 'rb').read(), byteorder='big')