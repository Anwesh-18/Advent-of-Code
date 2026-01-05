content = open("input1.txt","r").read()
lines = content.split("\n")

orbits = {}
orbits["COM"] = 0

while lines:
    line = lines.pop(0)
    a,b = line.split(")")
    if a in orbits:
        orbits[b] = orbits.get(a) + 1
    else:
        lines.append(line)

totalOrbits = 0

for key,value in orbits.items():
    totalOrbits += value

print(totalOrbits)