content = open("input.txt","r").read()

total = 0
for i in range(len(content)):
    to_look = content[i]
    idx = i
    limit = len(content)//2
    if to_look == content[(idx+limit)%len(content)]:
        # print(to_look)
        total += int(to_look)

print(total)