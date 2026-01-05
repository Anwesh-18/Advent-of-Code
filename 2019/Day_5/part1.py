content = open("input1.txt").read().strip().split(",")
mem = list(map(int, content))

i = 0
input_value = 1
while True:
    instruction = mem[i]

    opcode = instruction % 100
    mode1 = (instruction // 100) % 10
    mode2 = (instruction // 1000) % 10

    def get_value(param, mode):
        if mode == 0:
            return mem[param]
        elif mode == 1:
            return param

    if opcode == 1:
        a = get_value(mem[i+1], mode1)
        b = get_value(mem[i+2], mode2)
        dest = mem[i+3]
        mem[dest] = a + b
        i += 4

    elif opcode == 2:
        a = get_value(mem[i+1], mode1)
        b = get_value(mem[i+2], mode2)
        dest = mem[i+3]
        mem[dest] = a * b
        i += 4

    elif opcode == 3:
        dest = mem[i+1]
        mem[dest] = input_value
        i += 2

    elif opcode == 4:
        value = get_value(mem[i+1], mode1)
        print(value)
        i += 2

    else:
        break
