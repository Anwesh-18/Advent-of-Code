content = open("input.txt","r").read()
lines = content.split("\n")

grid = []

for line in lines:
    grid.append(list(line))

def check_neighbors(grid, i, j):
    neighbors_count = 0
    if i+1 < len(grid):
        if grid[i+1][j] == "#":
            neighbors_count += 1
    if j+1 < len(grid[0]):
        if grid[i][j+1] == "#":
            neighbors_count += 1
    if i-1 >= 0:
        if grid[i-1][j] == "#":
            neighbors_count += 1
    if j-1 >= 0:
        if grid[i][j-1] == "#":
            neighbors_count += 1
    if i+1 < len(grid) and j+1 < len(grid[0]):
        if grid[i+1][j+1] == "#":
            neighbors_count += 1
    if i-1 >= 0 and j-1 >= 0:
        if grid[i-1][j-1] == "#":
            neighbors_count += 1
    if i+1 < len(grid) and j-1 >= 0:
        if grid[i+1][j-1] == "#":
            neighbors_count += 1
    if i-1 >= 0 and j+1 < len(grid[0]):
        if grid[i-1][j+1] == "#":
            neighbors_count += 1

    return neighbors_count

for _ in range(100):
    temp = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                if check_neighbors(grid, i, j) == 2 or check_neighbors(grid, i, j) == 3:
                    temp[i][j] = '#'
                else:
                    temp[i][j] = '.'
            else:
                if check_neighbors(grid, i, j) == 3:
                    temp[i][j] = '#'
                else:
                    temp[i][j] = '.'

    grid = temp

count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            count += 1

print(count)