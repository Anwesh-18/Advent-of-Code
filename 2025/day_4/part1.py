content = open('input.txt','r').read()
lines = content.split('\n')

grid = []
for line in lines:
    temp = []
    for ch in line:
        temp.append(ch)
    grid.append(temp)

dirs = [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
papers = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '@':
            count = 0
            for dir in dirs:
                dx = i+dir[0]
                dy = j+dir[1]
                if 0<= dx < len(grid) and 0<= dy < len(grid[i]):
                    if grid[dx][dy] == '@':
                        count += 1

            if count < 4:
                papers += 1

print(papers)