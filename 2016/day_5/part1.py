import hashlib

door_id = open('input.txt', 'r').read()

found = 0
i=0
res = []
while found < 8:
    s = door_id+str(i)
    hashed_val = hashlib.md5(s.encode()).hexdigest()
    if hashed_val.startswith('00000'):
        found += 1
        res.append(hashed_val[5])
    i+=1

print("".join(res))

