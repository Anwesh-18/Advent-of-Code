content = open("input1.txt","r").read()
lines = content.split("\n")

def signalDet(lines, override_b=None):
    instructions = []

    for line in lines:
        words = line.split()

        dest = words[-1]

        # Skip original assignment to b if overriding
        if override_b is not None and dest == 'b':
            continue

        if len(words) == 3:
            instructions.append(("ASSIGN", words[0], None, dest))
        elif len(words) == 4:
            instructions.append(("NOT", words[1], None, dest))
        else:
            instructions.append((words[1], words[0], words[2], dest))

    # Add override instruction
    if override_b is not None:
        instructions.insert(0, ("ASSIGN", str(override_b), None, "b"))

    values = {}

    def get(v):
        if v is None:
            return None
        if v.isdigit():
            return int(v)
        return values.get(v)

    while instructions:
        op, a, b, dest = instructions.pop(0)

        va = get(a)
        vb = get(b)

        if va is None or (b and vb is None):
            instructions.append((op, a, b, dest))
            continue

        if op == "ASSIGN":
            values[dest] = va & 0xFFFF
        elif op == "NOT":
            values[dest] = (~va) & 0xFFFF
        elif op == "AND":
            values[dest] = (va & vb) & 0xFFFF
        elif op == "OR":
            values[dest] = (va | vb) & 0xFFFF
        elif op == "LSHIFT":
            values[dest] = (va << vb) & 0xFFFF
        elif op == "RSHIFT":
            values[dest] = (va >> vb) & 0xFFFF

    return values['a']

a1 = signalDet(lines)
print(a1)
a2 = signalDet(lines, override_b=a1)
print(a2)