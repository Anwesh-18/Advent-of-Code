from collections import Counter

content = open('input.txt').read()
lines = content.split('\n')

val = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

def is_real(line,check_sum):
    to_check = ""
    line = "".join(line)
    count = Counter(line)

    sorted_letters = sorted(count.items(),key=lambda x:(-x[1],x[0]))
    for k,v in sorted_letters:
        to_check += k
    # print(to_check)
    if to_check[:5] == check_sum:
        return True
    else:
        return False


def find_real(parts,sector_id,val):
    final = []
    for part in parts:
        new_val = ""
        for ch in part:
            new_val += chr(((val[ch] + sector_id)%26)+97)

        final.append(new_val)
    return final

res = []

for line in lines:
    line = line.split("-")
    sector_id = int(line[-1][:3])
    check_sum = line[-1][3:].strip("[]")
    if is_real(line,check_sum):
        final = find_real(line[:-1],sector_id,val)
        res.append((final,sector_id))

for part in res:
    if 'northpole' in "".join(part[0]):
        print(part)