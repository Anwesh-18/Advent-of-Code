content = open("input.txt","r").read()
lines = content.split("\n")

instructions = []

for line in lines:
    inst = line.split()
    if len(inst) == 2:
        instructions.append(inst)
    else:
        instructions.append([inst[0],inst[1].rstrip(',') ,int(inst[2])])

a = 1
b = 0
idx = 0
while idx < len(instructions):
    if instructions[idx][0] == "inc":
        if instructions[idx][1] == 'a':
            a += 1
        else:
            b += 1

        idx += 1

    elif instructions[idx][0] == "tpl":
        if instructions[idx][1] == 'a':
            a *= 3
        else:
            b *= 3

        idx += 1
    elif instructions[idx][0] == "hlf":
        if instructions[idx][1] == 'a':
            a //= 2
        else:
            b //= 2

        idx += 1
    elif instructions[idx][0] == "jmp":
        idx += int(instructions[idx][1])
    elif instructions[idx][0] == "jie":
        if instructions[idx][1] == 'a':
            if a % 2 == 0:
                idx += int(instructions[idx][2])
            else:
                idx += 1
        else:
            if b % 2 == 0:
                idx += int(instructions[idx][2])
            else:
                idx += 1
    else:
        if instructions[idx][1] == 'a':
            if a == 1:
                idx += int(instructions[idx][2])
            else:
                idx += 1
        else:
            if b == 1:
                idx += int(instructions[idx][2])
            else:
                idx += 1

print(b)