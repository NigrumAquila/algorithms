def writeKey(key, alg):
    root = 'keys/'; filename = typedText('Enter filename with key: ')
    
    if alg == 'RSA':
        pubkFile = open(root + alg.lower() + '.' + filename +'.pubk', 'wb')
        pkFile = open(root + alg.lower() + '.' + filename +'.pk', 'wb')
        for param in key['public']: pubkFile.write(param.encode() + ': '.encode() + str(hex(key['public'][param])[2:].upper()).encode() + '\n'.encode())
        for param in key['private']: pkFile.write(param.encode() + ': '.encode() + str(hex(key['private'][param])[2:].upper()).encode() + '\n'.encode())
        pubkFile.close(); pkFile.close()

    if alg == 'LRR':
        open(root + alg.lower() + '.' + filename + '.pk', 'w').write(key)

    if alg == 'EC':
        pubkFile = open(root + alg.lower() + '.' + filename + '.pubk', 'w')
        pkFile = open(root + alg.lower() + '.' + filename + '.pk', 'w')
        for dictKey in key['public']: pubkFile.write(dictKey + ': ' + str(hex(key['public'][dictKey])[2:]).upper() + '\n')
        for dictKey in key['private']: pkFile.write(dictKey + ': ' + str(hex(key['private'][dictKey])[2:]).upper() + '\n')
        pubkFile.close(); pkFile.close()

    if alg == 'EL_GAMAL':
        pubkFile = open(root + alg.lower() + '.' + filename +'.pubk', 'wb')
        pkFile = open(root + alg.lower() + '.' + filename +'.pk', 'wb')
        for param in key['public']: pubkFile.write(param.encode() + ': '.encode() + str(hex(key['public'][param])[2:].upper()).encode() + '\n'.encode())
        for param in key['private']: pkFile.write(param.encode() + ': '.encode() + str(hex(key['private'][param])[2:].upper()).encode() + '\n'.encode())
        pubkFile.close(); pkFile.close()
