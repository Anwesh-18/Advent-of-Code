content = open("input2.txt","r").read().splitlines()

count = 0
def isNice(line):
    first = False
    second = False

    # Checking the first condition
    for i in range(len(line)):
        look = line[i:i+2]
        for j in range(i+2,len(line)-1):
            if line[j:j+2]==look:
                first = True
                break

    # Checking the second condition
    for i in range(len(line)-2):
        if line[i] == line[i+2]:
            second = True
            break

    if first and second:
        return True
    return False

for line in content:
    if isNice(line):
        count += 1

print(count)