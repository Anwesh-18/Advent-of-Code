content = open("input.txt","r").read()
lines = content.split("\n")

unique = set()
transform = {}

for line in lines:
    if not line:
        break
    line = line.split()
    src = line[2]
    dest = line[0]
    if src not in transform:
        transform[src] = dest

molecule = lines[-1]
test = dict(sorted(transform.items(),key=lambda x: len(x[0]),reverse=True))
step = 0

while molecule != 'e':
    for src in test:
        start = 0
        if src in molecule:
            idx = molecule.find(src, start)
            if idx == -1:
                break
            molecule = molecule[:idx] + test[src] + molecule[idx + len(src):]
            step += 1

print(step)

