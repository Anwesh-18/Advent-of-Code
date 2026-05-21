line = open('input.txt', 'r').read()

dirs = {'N':[0,1],
       'S':[0,-1],
       'E':[1,0],
       'W':[-1,0]
       }
moves = line.split(", ")

curr_dir = [('W','E'),('N','S'),('E','W'),('S','N')]
idx=0
curr_pos = [(0,0)]

def make_move(curr_pos, m, dirs,dist):
    dx,dy = dirs[m]
    dx *= dist
    dy *= dist
    x,y = curr_pos[-1]
    new_x = x + dx
    new_y = y + dy
    curr_pos.append((new_x,new_y))

for move in moves:
    m = move[0]
    dist = int(move[1:])
    left,right = curr_dir[idx]
    if m == 'R':
        make_move(curr_pos,right,dirs,dist)
        idx = (idx + 1)%4
    else:
        make_move(curr_pos, left,dirs,dist)
        idx = (idx - 1)%4

x,y = curr_pos[-1]
res = abs(0-x)+abs(0-y)
print(res)