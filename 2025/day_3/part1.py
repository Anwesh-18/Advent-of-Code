content = open('input.txt','r').read()
lines = content.split('\n')

def find_jolt(line):
    maxVal = float('-inf')

    for i in range(len(line)):
        for j in range(i+1,len(line)):
            maxVal = max(maxVal,int(line[i]+line[j]))

    return maxVal

total = 0
for line in lines:
    total += find_jolt(line)

print(total)