import hashlib

word = open("input2.txt","r").read()
num = 1

while True:
    newEl = word + str(num)
    md5_Hash = hashlib.md5(newEl.encode()).hexdigest()

    if md5_Hash[:6] == "000000":
        print(num)
        break

    num += 1