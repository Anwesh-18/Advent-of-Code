content = open("input2.txt","r").read()
lines = content.split("\n")

grid = [[0]*1000 for _ in range(1000)]

def toggle(x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            grid[i][j] += 2

def onOff(x1,y1,x2,y2,command):
    if command == "on":
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                grid[i][j] += 1
    else:
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                grid[i][j] = max(grid[i][j]-1,0)

for line in lines:
    words = line.split(" ")
    if len(words) == 4:
        x1 = int(words[1].split(",")[0])
        y1 = int(words[1].split(",")[1])
        x2 = int(words[3].split(",")[0])
        y2 = int(words[3].split(",")[1])
        toggle(x1,y1,x2,y2)
    else:
        command = words[1]
        x1 = int(words[2].split(",")[0])
        y1 = int(words[2].split(",")[1])
        x2 = int(words[4].split(",")[0])
        y2 = int(words[4].split(",")[1])
        onOff(x1,y1,x2,y2,command)

count = 0
for i in range(1000):
    for j in range(1000):
        count += grid[i][j]

print(count)