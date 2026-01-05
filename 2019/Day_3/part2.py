content = open("input2.txt","r").read()
lines = content.split("\n")

def move_wire(directions):
    x, y = 0, 0
    steps = 0
    visited = {}

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

            steps += 1

            if (x, y) not in visited:
                visited[(x, y)] = steps

    return visited


wire1_dirs = lines[0].split(",")
wire2_dirs = lines[1].split(",")

wire1 = move_wire(wire1_dirs)
wire2 = move_wire(wire2_dirs)

intersections = wire1.keys() & wire2.keys()

res = float('inf')

for pos in intersections:
    first_wire = wire1[pos]
    second_wire = wire2[pos]
    res = min(res,first_wire+second_wire)

print(res)
