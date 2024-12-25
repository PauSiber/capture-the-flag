from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad,unpad
import os
from datetime import datetime
import random

# safe key, trust
key = '00000000000000000000000000000000' 

def split_file(file, offset):
    
    file1 = file[:offset]
    file2 = file[offset:]

    return file1, file2

def getTimestamp():
    # 26 Aug 2024 21:43:20 UTC
    return 1724708600

def gen_offset():
    super_safe_seed = getTimestamp()
    random.seed(super_safe_seed)
    return random.randint(5000, 5500)

def get_all_aes_modes():

    modes = [
        AES.MODE_ECB,
        AES.MODE_CBC,
        AES.MODE_CFB,
        AES.MODE_OFB,
        AES.MODE_CTR,
        AES.MODE_OPENPGP,
        AES.MODE_CCM,
        AES.MODE_EAX,
        AES.MODE_SIV,
        AES.MODE_GCM,
        AES.MODE_OCB
    ]

    return modes

def decrypt(enc, aes_modes):

    for mode in aes_modes:

        try:
            cipher = AES.new(key.encode('utf-8'), mode)
            return unpad(cipher.decrypt(enc),16)

        except:
            continue


file = open("encrypted.png", "rb").read()

# key is 32 byte which is 256 bit
offset = gen_offset() * 256

file1, encrypted_part = split_file(file, offset)

aes_modes = get_all_aes_modes()

decrypted_part = decrypt(encrypted_part, aes_modes)

file = open("decrypted.png", "wb")

file.write(file1 + decrypted_part)



