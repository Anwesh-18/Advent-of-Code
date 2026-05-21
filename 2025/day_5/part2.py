content = open('input.txt','r').read()
lines = content.split('\n')

ranges = []
valid_ids = []

for line in lines:
    if line.strip() == "":
        break

    start, end = map(int,line.split('-'))
    ranges.append((start,end))

ranges.sort()
for s,e in ranges:
    if not valid_ids or s > valid_ids[-1][1]+1:
        valid_ids.append([s,e])
    else:
        valid_ids[-1][1] = max(valid_ids[-1][1],e)

total = 0
for s,e in valid_ids:
    total += (e-s+1)

print(total)