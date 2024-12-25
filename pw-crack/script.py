import hashlib
 
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################
 
key = "E676"
flag = "P4U$1B3R_CTF{D1CT1ONARY_@TT@CK}"

flag_enc = open('flag.txt.enc', 'rb').read()
correct_pw_hash = open('hash.bin', 'rb').read()
 
def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()
 
 
def level_5_pw_check():
    #user_pw = input("Please enter correct password for flag: ")
    user_pw = key
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")


def gen_dict():
    dict_file = open('dictionary.txt', 'w')

    for i in range(2**16):
        pw = f"{i:04X}"
        dict_file.writelines(pw + "\n")


def print_dict():
    dict_file = open('dictionary.txt', 'r')

    for hex in dict_file:
        print(hex.strip())


def gen_hash_bin():
    hash = hash_pw(key)
    hash_file = open('hash.bin', 'wb')
    hash_file.write(hash)


def gen_flag_txt():
    flag_enc = str_xor(flag, key)
    flag_file = open('flag.txt.enc', 'w')
    flag_file.write(flag_enc)


level_5_pw_check()