content = open("input.txt","r").read()

total = 0
for i in range(len(content)):
    # print(content[i])
    if content[i] == content[(i+1)%len(content)]:
        total += int(content[i])

print(total)