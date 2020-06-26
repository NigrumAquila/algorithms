def generateGamma(shift_register_state, taps):
    xor_input = 1; nbits = shift_register_state.bit_length()
    for tap in taps:
        if (shift_register_state & (1<<(tap-1))) != 0:
            xor_input ^= 1
    shift_register_state = (xor_input << nbits-1) + (shift_register_state >> 1)
    return shift_register_state

shift_register_state = int(generateKey())
shift_register_state = 11001010
cipher = ''
encoded = ''

# file = open('data/text.txt')
# for char in file.read():
#     gamma = generateGamma(shift_register_state, taps)
#     shift_register_state = gamma
#     cipherChar = gamma ^ ord(char)
#     cipherChar = ord(char) ^ gamma
#     encodedChar = gamma ^ cipherChar
#     cipher += str(cipherChar)
#     encoded += chr(encodedChar)
#     print(char, cipherChar, encodedChar, chr(encodedChar))
    # exit('kek')

# file.close()

# print(cipher)
# print(encoded)