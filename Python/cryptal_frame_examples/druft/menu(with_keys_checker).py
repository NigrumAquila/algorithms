from src.fileHelpers import fileHelpers


while True:
    case = input('Select action: 1 - RSA; 2 - Linear recurrent register; "e" - to exit: ')
    if case == '1':
        from src.RSA import RSA
        while True:
            case = input('Select action: 1 - Generate keys; 2 - Encode file; 3 - Decode file; "e" - to exit: ')
            if case == '1':
                # keys = RSA.generateKeys()
                # writeKeys(keys, 'rsa')RSA.generateKeys()
                writeKeys(RSA.generateKeys(), 'rsa')
                print('Keys generated.')
            elif case == '2':
                if not 'keys' in locals(): print('Key is not defined.'); continue
                if keys == '': print('Key is empty.'); continue
                cipher = RSA.encrypt(readKey('rsa', 'public'), open('data/text.txt').read())
                f = open('data/cipher', 'w')
                for cipherChar in cipher:
                    f.write(cipherChar)
                f.close()
                print('File encrypted.', cipher)
            elif case == '3':
                if not 'keys' in locals(): print('Key is not defined.'); continue
                if keys == '': print('Key is empty.'); continue
                decrypted = RSA.decrypt(readKey('rsa', 'private'), open('data/cipher'))
                print('File decrypted.', decrypted)
            elif case == 'e':
                exit('Execution completed.')
            else:
                print('Wrong selection. Please, try again.')
    elif case == '2':
        while True:
            case = input('Select action: 1 - Generate key; 2 - Encode file; 3 - Decode file; "e" - to exit: ')
            if case == '1':
                print('Keys generated.')
            elif case == '2':
                if not 'keys' in locals(): print('Key is not defined.'); continue
                if keys == '': print('Key is empty.'); continue
                print('File encrypted.')
            elif case == '3':
                if not 'keys' in locals(): print('Key is not defined.'); continue
                if keys == '': print('Key is empty.'); continue
                print('File decrypted.')
            elif case == 'e':
                exit('Execution completed.')
            else:
                print('Wrong selection. Please, try again.')
    elif case == 'e':
        exit('Execution completed.')
    else:
        print('Wrong selection. Please, try again.')


