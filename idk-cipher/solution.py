
import base64

srt_key = 'secretkey'
b64_enc_val = "Iw5RMTYRVuKDnlQ1NgxY4oOHNzom4oOVMAAxFyXig48JBBfig4k="


b64_dec_val = base64.b64decode(b64_enc_val)

decoded_val = b64_dec_val.decode()

output_arr = list(decoded_val)

usr_input = []
rsv_input = []

for i in range(0, int(len(output_arr) / 2)):
    enc_p1 = ord(output_arr[i*2])
    enc_p2 = ord(output_arr[(i*2) + 1])

    # XOR operation can be reversable
    c1 = ord(srt_key[i % len(srt_key)]) ^ enc_p1
    c2 = ord(srt_key[i % len(srt_key)]) ^ enc_p2

    usr_input.append(chr(c1))
    rsv_input.append(chr(c2))

output_arr = usr_input + rsv_input[::-1]

print("".join(output_arr))

