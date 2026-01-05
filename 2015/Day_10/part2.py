content = open("input.txt","r").read()
sequence = content

def cal_next(line):
    res = []
    count = 1
    for i in range(1,len(line)):
        if line[i-1] == line[i]:
            count += 1
        else:
            res.append(str(count))
            res.append(line[i-1])
            count = 1

    res.append(str(count))
    res.append(line[-1])

    return "".join(res)

for i in range(50):
    sequence = cal_next(sequence)

print(len(sequence))