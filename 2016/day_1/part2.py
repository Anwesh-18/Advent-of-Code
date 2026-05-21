line = open('input.txt', 'r').read()

dirs = {'N':[0,1],
       'S':[0,-1],
       'E':[1,0],
       'W':[-1,0]
       }
moves = line.split(", ")

curr_dir = [('W','E'),('N','S'),('E','W'),('S','N')]
idx=0
visited = set()
visited.add((0,0))
curr_pos = [(0,0)]
j=1
def make_move(curr_pos, m, dirs,dist):
    global j
    dx,dy = dirs[m]
    x1,y1 = curr_pos[-1]
    for i in range(dist):
        x1+=dx
        y1+=dy
        new_point = (x1,y1)
        if new_point in visited:
            dist = abs(0-x1)+abs(0-y1)
            print(f'visited {j}th time: {new_point} and dist: {dist}')
            j+=1
        visited.add(new_point)
        curr_pos[0] = new_point

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

