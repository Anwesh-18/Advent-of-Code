content = open('input.txt','r').read()
lines = content.split('\n')

grid = [[1,2,3],
        [4,5,6],
        [7,8,9]]

dirs = {'U':[-1,0],
        'D':[1,0],
        'L':[0,-1],
        'R':[0,1]}

curr_pos = [1,1]
res = []
def move(grid,dirs,direction):
    global curr_pos
    dx,dy = dirs[direction]
    x,y = curr_pos[0],curr_pos[1]
    if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]):
        new_x = x + dx
        new_y = y + dy
        curr_pos = [new_x,new_y]

def process_line(line,grid,dirs):
    for ch in line:
        if ch == 'U':
            move(grid,dirs,'U')
        elif ch == 'D':
            move(grid,dirs,'D')
        elif ch == 'L':
            move(grid,dirs,'L')
        else:
            move(grid,dirs,'R')

    return grid[curr_pos[0]][curr_pos[1]]


for line in lines:
    res.append(str(process_line(line,grid,dirs)))

print(''.join(res))