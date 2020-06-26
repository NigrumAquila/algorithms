from ..helpers.fileHelpers import pickFileForEncrypt, pickFileForDecrypt


class LRR:
    NBYTES = 1
    TAPS = (8,7,6,1)

    generateKey = staticmethod(lambda: bin(int.from_bytes(getattr(__import__('os'), 'urandom')(LRR.NBYTES), byteorder='big'))[2:])
    
    @staticmethod
    def generateGamma(shift_register_state):
        xor_input = 1; nbits = shift_register_state.bit_length()
        for tap in LRR.TAPS:
            if (shift_register_state & (1<<(tap-1))) != 0:
                xor_input ^= 1
        shift_register_state = (xor_input << nbits-1) + (shift_register_state >> 1)
        return shift_register_state

    @staticmethod
    def encrypt(seed):
        srcFile, dstFile = pickFileForEncrypt()
        shift_register_state = int(seed)

        while True:
            char = srcFile.read(1)
            if not char: break
            gamma = LRR.generateGamma(shift_register_state)
            shift_register_state = gamma
            cipherChar = gamma ^ int.from_bytes(char, byteorder='big')
            cipherBytes = cipherChar.to_bytes(16, byteorder='big')
            dstFile.write(cipherBytes)
        srcFile.close(); dstFile.close()

        # for char in srcFile.read(1):
        #     gamma = LRR.generateGamma(shift_register_state)
        #     shift_register_state = gamma
        #     # cipherChar = gamma ^ int.from_bytes(char, byteorder='big')
        #     cipherChar = gamma ^ char
        #     cipherBytes = cipherChar.to_bytes(16, byteorder='big')
        #     dstFile.write(cipherBytes)
        # srcFile.close(); dstFile.close()
    
    @staticmethod
    def decrypt(seed):
        srcFile, dstFile = pickFileForDecrypt()
        shift_register_state = int(seed)

        while True:
            char = srcFile.read(16)
            if not char: break
            gamma = LRR.generateGamma(shift_register_state)
            shift_register_state = gamma
            decryptedChar = gamma ^ int.from_bytes(char, byteorder='big')
            decryptedByte = decryptedChar.to_bytes(1, byteorder='big')
            dstFile.write(decryptedByte)
        srcFile.close(); dstFile.close()

        # for char in srcFile.read(1):
        #     gamma = LRR.generateGamma(shift_register_state)
        #     shift_register_state = gamma
        #     decryptedChar = gamma ^ char
        #     print(char, decryptedChar)
        #     exit()
        #     decryptedByte = decryptedChar.to_bytes(1, byteorder='big')
        #     dstFile.write(decryptedByte)
        # srcFile.close(); dstFile.close()