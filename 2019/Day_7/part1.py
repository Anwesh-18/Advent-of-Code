import itertools

def Intcode(inputs, content):
    mem = list(map(int, content))
    i = 0
    input_ptr = 0
    output = None

    def get_value(param, mode):
        return mem[param] if mode == 0 else param

    while True:
        instruction = mem[i]
        opcode = instruction % 100
        mode1 = (instruction // 100) % 10
        mode2 = (instruction // 1000) % 10

        if opcode == 1:
            mem[mem[i + 3]] = get_value(mem[i + 1], mode1) + get_value(mem[i + 2], mode2)
            i += 4

        elif opcode == 2:
            mem[mem[i + 3]] = get_value(mem[i + 1], mode1) * get_value(mem[i + 2], mode2)
            i += 4

        elif opcode == 3:
            mem[mem[i + 1]] = inputs[input_ptr]
            input_ptr += 1
            i += 2

        elif opcode == 4:
            output = get_value(mem[i + 1], mode1)
            i += 2

        elif opcode == 5:
            if get_value(mem[i + 1], mode1) != 0:
                i = get_value(mem[i + 2], mode2)
            else:
                i += 3

        elif opcode == 6:
            if get_value(mem[i + 1], mode1) == 0:
                i = get_value(mem[i + 2], mode2)
            else:
                i += 3

        elif opcode == 7:
            mem[mem[i + 3]] = 1 if get_value(mem[i + 1], mode1) < get_value(mem[i + 2], mode2) else 0
            i += 4

        elif opcode == 8:
            mem[mem[i + 3]] = 1 if get_value(mem[i + 1], mode1) == get_value(mem[i + 2], mode2) else 0
            i += 4

        else:
            return output

content = open("input1.txt").read().strip().split(",")

max_signal = 0

for perm in itertools.permutations([0,1,2,3,4]):
    signal = 0
    for phase in perm:
        signal = Intcode([phase, signal], content)
    max_signal = max(max_signal, signal)

print(max_signal)
