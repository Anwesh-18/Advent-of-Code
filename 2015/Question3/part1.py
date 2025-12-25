file = open("input1.txt", "r")
content = file.read()
file.close()

count = 1

x = 0
y = 0

visited = set()
visited.add((x,y))

for char in content:
    if char == "^":
        x -= 1
        if (x,y) not in visited:
            count += 1
            visited.add((x,y))
    elif char == "v":
        x += 1
        if (x,y) not in visited:
            count += 1
            visited.add((x,y))
    elif char == "<":
        y -= 1
        if (x,y) not in visited:
            count += 1
            visited.add((x,y))
    else:
        y += 1
        if (x,y) not in visited:
            count += 1
            visited.add((x,y))

print(count)