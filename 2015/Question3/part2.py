file = open("input2.txt", "r")
content = file.read()
file.close()

count = 1

x1 = 0
y1 = 0

x2 = 0
y2 = 0

visited = set()
visited.add((0,0))
turn = True

def santa(char):
    global x1
    global y1
    global count
    if char == "^":
        x1 -= 1
        if (x1,y1) not in visited:
            count += 1
            visited.add((x1,y1))
    elif char == "v":
        x1 += 1
        if (x1,y1) not in visited:
            count += 1
            visited.add((x1,y1))
    elif char == "<":
        y1 -= 1
        if (x1,y1) not in visited:
            count += 1
            visited.add((x1,y1))
    else:
        y1 += 1
        if (x1,y1) not in visited:
            count += 1
            visited.add((x1,y1))

def roboSanta(char):
    global x2
    global y2
    global count
    if char == "^":
        x2 -= 1
        if (x2,y2) not in visited:
            count += 1
            visited.add((x2,y2))
    elif char == "v":
        x2 += 1
        if (x2,y2) not in visited:
            count += 1
            visited.add((x2,y2))
    elif char == "<":
        y2 -= 1
        if (x2,y2) not in visited:
            count += 1
            visited.add((x2,y2))
    else:
        y2 += 1
        if (x2,y2) not in visited:
            count += 1
            visited.add((x2,y2))

for char in content:
    if turn:
        santa(char)
    else:
        roboSanta(char)

    turn = not turn

print(count)