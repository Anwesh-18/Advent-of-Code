content = open('input.txt').read()
lines = content.split('\n')

grid = [['.']*50 for _ in range(6)]

def rect(col,row,grid):
    for i in range(row):
        for j in range(col):
            grid[i][j] = '#'

def rotate_col(col,dist,grid):
    dist %= 6
    column = [grid[r][col] for r in range(6)]
    column = column[-dist:] + column[:-dist]
    for r in range(6):
        grid[r][col] = column[r]

def rotate_row(row,dist,grid):
    dist %= 50
    new_row = grid[row][-dist:] + grid[row][:-dist]
    grid[row] = new_row


for line in lines:
    line = line.split()
    if len(line) == 2:
        col,row = map(int,line[1].split('x'))
        rect(col,row,grid)
    else:
        dim = line[1]
        if dim == 'row':
            row = int(line[2][2:])
            dist = int(line[4])
            rotate_row(row,dist,grid)
        else:
            col = int(line[2][2:])
            dist = int(line[4])
            rotate_col(col,dist,grid)

for i in range(6):
    print(''.join(grid[i]))

count = sum(row.count('#') for row in grid)
print(count)