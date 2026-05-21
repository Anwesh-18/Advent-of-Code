content = open('input.txt').read()
lines = content.split('\n')

bots = {}

def check_bot(bots,b_num):
    if 61 in bots[b_num] and 17 in bots[b_num]:
        return True
    return False

instrs = []

for line in lines:
    parts = line.split()
    if len(parts) == 6:
        if int(parts[5]) in bots:
            bots[int(parts[5])].append(int(parts[1]))
        else:
            bots[int(parts[5])] = [int(parts[1])]

    else:
        instrs.append(parts)

for inst in instrs:
    nums = int(inst[1])
    to_give_low,low = int(inst[6])
    high = int(inst[11])