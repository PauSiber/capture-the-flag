def gen_xor_key(flag):
    xor_key = ""
    cipher = 0
    for i in range(len(flag)):
        xor_key += str(cipher)
        cipher = ~cipher
    return xor_key


flag = "PAUS1B3R_CTF{cmon_be_more_creative_man}"
xor_key = gen_xor_key(flag)

cipher_flag = bytearray([b1 ^ b2 for b1, b2 in zip(flag.encode(), xor_key.encode())])

file = open("cipher_flag.txt","wb")

file.write(cipher_flag)
