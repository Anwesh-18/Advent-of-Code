content = open("input1.txt","r").read()
lines = content.split("\n")

instructions = []

for line in lines:
    words = line.split(" ")
    if len(words) == 3: #123 -> x
        instructions.append(("ASSIGN",words[0],None,words[2]))
    elif len(words) == 4: #NOT x -> y
        instructions.append(("NOT",words[1],None,words[3]))
    else: # x AND y -> z
        instructions.append((words[1], words[0], words[2], words[4]))

values = {}

def get(v):
    if v is None:
        return None
    if v.isdigit():
        return int(v)
    return values.get(v)

while instructions:
    op,a,b,dest = instructions.pop(0)

    va = get(a)
    vb = get(b)

    if va is None or (vb is None and op != "NOT" and op != "ASSIGN"):
        instructions.append((op,a,b,dest))
        continue

    if op == "ASSIGN":
        values[dest] = va
    elif op == "NOT":
        values[dest] = 65535 - va
    elif op == "AND":
        values[dest] = va & vb
    elif op == "OR":
        values[dest] = va | vb
    elif op == "LSHIFT":
        values[dest] = va << vb
    elif op == "RSHIFT":
        values[dest] = va >> vb

print(values['a'])