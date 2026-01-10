content = open("input.txt","r").read()
lines = content.split("\n")

unique = set()
transform = []

for line in lines:
    if not line:
        break
    line = line.split()
    dest = line[2]
    src = line[0]
    transform.append((src,dest))

molecule = lines[-1]

for src,dest in transform:
    start = 0
    while True:
        idx = molecule.find(src,start)
        if idx == -1:
            break

        unique.add(molecule[:idx]+dest+molecule[idx+len(src):])
        start = idx+1

print(len(unique))
