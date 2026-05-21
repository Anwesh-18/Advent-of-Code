import hashlib

door_id = open('input.txt', 'r').read()

found = 0
i=0
res = [None]*8
while found < 8:
    s = door_id+str(i)
    hashed_val = hashlib.md5(s.encode()).hexdigest()
    if hashed_val.startswith('00000'):
        pos = hashed_val[5]
        if pos.isdigit():
            idx = int(pos)
            if idx < 8 and res[idx] is None:
                res[idx] = hashed_val[6]
                found += 1
    i+=1

print("".join(res))

