def lfsr(seed, mask):
    result = seed
    nbits = mask.bit_length()-1
    while True:
        result = (result << 1)
        xor = result >> nbits
        if xor != 0:
            result ^= mask

        yield xor, result


seed = 0b11001001
taps = 0b00000001
for xor, sr in lfsr(seed, taps):
    nbits = seed.bit_length()
    print(xor, bin(2**nbits+sr)[3:], bin(sr), sr)
    exit()
    pass