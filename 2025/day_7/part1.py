content = open('input.txt', 'r').read()
lines = content.split('\n')

grid = []
count = 0

for line in lines:
    temp = []
    for ch in line:
        temp.append(ch)
    grid.append(temp)

# for i in range(len(grid)):
#     print("".join(grid[i]))

for i in range(1,len(grid)):
    for j in range(len(grid[i])):
        if grid[i-1][j] == 'S':
            grid[i][j] = '|'

        if grid[i][j] == '^':
            if grid[i-1][j] == '|':
                grid[i][j-1] = '|'
                grid[i][j+1] = '|'
                count += 1

        else:
            if grid[i-1][j] == '|':
                grid[i][j] = '|'

# for i in range(len(grid)):
#     print("".join(grid[i]))

print(count)