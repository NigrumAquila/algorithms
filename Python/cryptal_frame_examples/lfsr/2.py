def lfsr2(seed, taps):
    #xor_input - вдвигаемый бит
    shift_register_state = seed; xor_input = 1; nbits = seed.bit_length()
    while True:
        for tap in taps:
            #проверяем значение отводного разряда, если разряд = 1; то меняем значение вдвигаемого бита, иначе проверяемый следующий разряд
            if (shift_register_state & (1<<(tap-1))) != 0:
                xor_input ^= 1
        #(xor << nbits-1) - 1000 0000 or 0000 0000; вдвигается левый бит
        #sr >> 1 - сдвигаются все биты направо на 1; складываем значение регистра с вдвигаемым битом
        shift_register_state = (xor_input << nbits-1) + (shift_register_state >> 1)
        yield xor_input, shift_register_state
        #если дошли до периода, заканчиваем выполнение;
        if shift_register_state == seed:
            break



seed = 0b11001001
taps = (8,7,6,1)
for xor_input, shift_register_state in lfsr2(seed, taps):
    nbits = seed.bit_length()
    text = ord('s')
    cipher = shift_register_state ^ text
    encoded = shift_register_state ^ cipher
    print(xor_input, bin(2**nbits+shift_register_state)[3:], shift_register_state, text, cipher, encoded)
    exit()
    pass


# for x in range(1,8):
#     print('1 xor', x, '=', 1^x)

# for x in range(8,0,-1):
#     print('0b11001001 & (1<<(' + str(x), '- 1)):',  0b11001001 & (1<<(x-1)))

