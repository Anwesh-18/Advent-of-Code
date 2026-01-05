with open("input.txt", "r") as f:
    data = f.read().strip()

floor = 0
for i,char in enumerate(data,start=1):
    if char == "(":
        floor += 1
    else:
        floor -= 1

    if floor == -1:
        print(i)
        break

print(floor)