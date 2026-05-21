with open("input.txt","r") as f:
    content = f.read()

res = 0

left,right = [],[]
lines = content.split()
turn = 1
for line in lines:
    if turn:
        left.append(int(line))
    else:
        right.append(int(line))
    turn = 1-turn

left.sort()
right.sort()

for i in range(len(left)):
    res += abs(left[i]-right[i])

print(res)