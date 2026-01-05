content = open("input2.txt","r").read()
original = list(map(int, content.split(",")))

def outPut(mem):
    i = 0
    while mem[i] != 99:
        if mem[i] == 1:
            mem[mem[i + 3]] = mem[mem[i + 1]] + mem[mem[i + 2]]
        elif mem[i] == 2:
            mem[mem[i + 3]] = mem[mem[i + 1]] * mem[mem[i + 2]]
        else:
            raise ValueError("Invalid opcode")
        i += 4
    return mem[0]

for noun in range(100):
    for verb in range(100):
        mem = original.copy()
        mem[1] = noun
        mem[2] = verb

        res = outPut(mem)

        if res == 19690720:
            print("Part 2:", 100 * noun + verb)
            exit(0)
