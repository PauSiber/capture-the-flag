import base64

file1 = open("32_1.txt","r").read()
file2 = open("32_2.txt","r").read()

for i in range(32):
    file1 = base64.b64decode(file1)

for i in range(32):
    file2 = base64.b64decode(file2)


file = open("flag.txt","wb")

file.write(file1 + file2)
