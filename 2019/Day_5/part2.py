content = open("input1.txt").read().strip().split(",")
mem = list(map(int, content))

i = 0
input_value = 5

def get_value(param, mode):
    if mode == 0:
        return mem[param]
    elif mode == 1:
        return param

while True:
    instruction = mem[i]

    opcode = instruction % 100
    mode1 = (instruction // 100) % 10
    mode2 = (instruction // 1000) % 10

    if opcode == 1:
        a = get_value(mem[i+1], mode1)
        b = get_value(mem[i+2], mode2)
        mem[mem[i+3]] = a + b
        i += 4

    elif opcode == 2:
        a = get_value(mem[i+1], mode1)
        b = get_value(mem[i+2], mode2)
        mem[mem[i+3]] = a * b
        i += 4

    elif opcode == 3:
        mem[mem[i+1]] = input_value
        i += 2

    elif opcode == 4:
        print(get_value(mem[i+1], mode1))
        i += 2

    elif opcode == 5:
        if get_value(mem[i+1], mode1) != 0:
            i = get_value(mem[i+2], mode2)
        else:
            i += 2 + 1

    elif opcode == 6:
        if get_value(mem[i+1], mode1) == 0:
            i = get_value(mem[i+2], mode2)
        else:
            i += 2 + 1

    elif opcode == 7:
        mem[mem[i+3]] = 1 if get_value(mem[i+1], mode1) < get_value(mem[i+2], mode2) else 0
        i += 4

    elif opcode == 8:
        mem[mem[i+3]] = 1 if get_value(mem[i+1], mode1) == get_value(mem[i+2], mode2) else 0
        i += 4

    else:
        break