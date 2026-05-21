content = int(open("input.txt").read())

x, y = 0, 0
value = 1
seen = {(0,0):1}

directions = [(1,0), (0,1), (-1,0), (0,-1)]
dir_idx = 0
step_len = 1

def adj_sum(x,y):
    total = 0
    if (x-1,y) in seen:
        total += seen[(x-1,y)]
    if (x,y-1) in seen:
        total += seen[(x,y-1)]
    if (x+1,y) in seen:
        total += seen[(x+1,y)]
    if (x,y+1) in seen:
        total += seen[(x,y+1)]
    if (x-1,y-1) in seen:
        total += seen[(x-1,y-1)]
    if (x+1,y+1) in seen:
        total += seen[(x+1,y+1)]
    if (x-1,y+1) in seen:
        total += seen[(x-1,y+1)]
    if (x+1,y-1) in seen:
        total += seen[(x+1,y-1)]

    return total

while value < content:
    for _ in range(2):
        dx, dy = directions[dir_idx]
        for _ in range(step_len):
            if value >= content:
                break
            x += dx
            y += dy
            value = adj_sum(x,y)
            print(value)
            seen[(x,y)] = value

        dir_idx = (dir_idx + 1) % 4

    step_len += 1

print(value)