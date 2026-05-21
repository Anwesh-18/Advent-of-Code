from collections import deque

content = open("input.txt","r").read()
lines = content.split("\n")

grid = []

for line in lines:
    temp = []
    for i in range(len(line)):
        temp.append(line[i])
    grid.append(temp)

start = 0
for i in range(len(grid)):
    found = False
    for j in range(len(grid[i])):
        if grid[i][j] == '@':
            start = (i,j)
            found = True
            break
    if found:
        break

# def search(row,col,grid):
#