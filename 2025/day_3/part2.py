from itertools import combinations

content = open('input.txt','r').read()
lines = content.split('\n')

def find_jolt(line,k):
    to_remove = len(line) - k
    stack = []
    for c in line:
        while stack and to_remove > 0 and int(stack[-1]) < int(c):
            stack.pop()
            to_remove -= 1
        stack.append(c)

    while to_remove > 0:
        stack.pop()
        to_remove -= 1

    return int(''.join(stack))

total = 0
for line in lines:
    total += find_jolt(line,12)
    # print(line)

print(total)