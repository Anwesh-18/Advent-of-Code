import hashlib

word = open("input1.txt","r").read()
print(word)
num = 1

while True:
    newEl = word + str(num)
    md5_hash = hashlib.md5(newEl.encode()).hexdigest()

    if md5_hash[:5] == "00000":
        print(num)
        print(newEl)
        print(md5_hash)
        break

    num += 1