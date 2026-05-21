content = open('input.txt','r').read()
lines = content.split('\n')

res = []
set_len = True

def mul(nums):
    tm = 1
    for num in nums:
        tm *= num
    return tm

def compute(res):
    total = 0
    for op in res:
        if op[-1] == '+':
            total += sum(op[:-1])
        if op[-1] == '*':
            total += mul(op[:-1])

    return total

for line in lines:
    line = line.split()
    if set_len:
        for i in range(len(line)):
            temp = [int(line[i])]
            res.append(temp)

        set_len = False

    else:
        for i in range(len(line)):
            if line[i] == '+' or line[i] == '*':
                res[i].append(line[i])
            else:
                res[i].append(int(line[i]))


print(compute(res))