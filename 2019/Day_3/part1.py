content = open("input1.txt","r").read()
lines = content.split("\n")

def move_wire(directions):
    x, y = 0, 0
    visited = set()

    for direction in directions:
        move = int(direction[1:])
        d = direction[0]

        for _ in range(move):
            if d == 'R':
                x += 1
            elif d == 'L':
                x -= 1
            elif d == 'U':
                y += 1
            elif d == 'D':
                y -= 1

            visited.add((x, y))

    return visited


wire1_dirs = lines[0].split(",")
wire2_dirs = lines[1].split(",")

wire1_path = move_wire(wire1_dirs)
wire2_path = move_wire(wire2_dirs)

intersections = wire1_path & wire2_path

minDist = float("inf")

for pos in intersections:
    x,y = pos
    dist = abs(x) + abs(y)
    minDist = min(minDist,dist)

print(minDist)
