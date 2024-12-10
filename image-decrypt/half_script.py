from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad,unpad
import os
from datetime import datetime
import random

# safe key, trust
key = '00000000000000000000000000000000' 

def gen_offset():
    super_safe_seed = int(datetime.utcnow().timestamp())
    random.seed(super_safe_seed)
    return random.randint(5000, 5500)

def encrypt(raw):
    raw = pad(raw,16)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_[!bozulmuş!])
    return cipher.encrypt(raw)

def decrypt(enc):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_[!bozulmuş!])
    return unpad(cipher.decrypt(enc),16)

### encrypted past this point, sorry!