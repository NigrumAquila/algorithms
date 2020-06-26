from src.helpers.fileHelpers import writeKey, readKey


while True:
    case = input('Select action: 1 - RSA; 2 - Linear recurrent register; "e" - to exit: ')
    if case == '1':
        from src.algorithms.RSA import RSA

        while True:
            case = input('Select action: 1 - Generate keys; 2 - Select public key; 3 - Select private key; 4 - Encode file; 5 - Decode file; "e" - to exit: ')

            if case == '1':
                writeKey(RSA.generateKeys(), 'rsa')
                print('Keys generated.')

            elif case == '2':

                pubKey = readKey('rsa', 'public')
                print('Public key selected. You can encrypt.')

            elif case == '3':
                privKey = readKey('rsa', 'private')
                print('Private key selected. You can decrypt.')

            elif case == '4':
                if not 'pubKey' in locals(): print('Key is not defined.'); continue
                if pubKey == '': print('Key is empty.'); continue
                data = open('data/text.txt').read()[3:]
                cipher = RSA.encrypt(pubKey, int(data))
                
                cipherFile = open('data/cipher', 'w')
                for cipherChar in str(cipher):
                    cipherFile.write(cipherChar)
                cipherFile.close()

                print('File encrypted.')

            elif case == '5':
                if not 'privKey' in locals(): print('Key is not defined.'); continue
                if privKey == '': print('Key is empty.'); continue
                cipher = open('data/cipher', 'r').read()
                decrypted = RSA.decrypt(privKey, int(cipher))
                print('File decrypted.', decrypted)

            elif case == 'e':
                exit('Execution completed.')

            else:
                print('Wrong selection. Please, try again.')

    elif case == '2':
        from src.algorithms.LRR import LRR

        while True:
            case = input('Select action: 1 - Generate key; 2 - Select key; 3 - Encode file; 4 - Decode file; "e" - to exit: ')

            if case == '1':
                writeKey(LRR.generateKey(), 'lrr')
                print('Key generated.')

            elif case == '2':
                key = readKey('lrr')
                print('Key selected.')
            
            elif case == '3':
                LRR.encrypt(key)
                print('File encrypted.')

            elif case == '4':
                LRR.decrypt(key)
                print('File decrypted.')

            elif case == 'e':
                exit('Execution completed.')

            else:
                print('Wrong selection. Please, try again.')

    elif case == 'e':
        exit('Execution completed.')

    else:
        print('Wrong selection. Please, try again.')
