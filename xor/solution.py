def gen_xor_key(flag):
    xor_key = ""
    cipher = 0
    for i in range(len(flag)):
        xor_key += str(cipher)
        cipher = ~cipher
    return xor_key

file = open("cipher_flag.txt","r")

cipher_text = file.read()
xor_key = gen_xor_key(cipher_text)

flag = bytearray([b1 ^ b2 for b1, b2 in zip(cipher_text.encode(), xor_key.encode())])

print(flag.decode("utf-8"))


