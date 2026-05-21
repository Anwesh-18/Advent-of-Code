content = open('input.txt', 'r').read().strip()
lines = content.split('\n')

points = []
for line in lines:
    x, y = line.split(',')
    points.append((int(y), int(x)))  # (row, col)

n = len(points)

allowed = set()

for i in range(n):
    r1, c1 = points[i]
    r2, c2 = points[(i + 1) % n]

    allowed.add((r1, c1))

    if r1 == r2:
        step = 1 if c2 > c1 else -1
        for c in range(c1 + step, c2, step):
            allowed.add((r1, c))
    else:
        step = 1 if r2 > r1 else -1
        for r in range(r1 + step, r2, step):
            allowed.add((r, c1))

rows = [r for r, c in allowed]
cols = [c for r, c in allowed]

min_r, max_r = min(rows), max(rows)
min_c, max_c = min(cols), max(cols)

for r in range(min_r, max_r + 1):
    cols_in_row = sorted(c for rr, c in allowed if rr == r)
    for i in range(0, len(cols_in_row) - 1, 2):
        for c in range(cols_in_row[i], cols_in_row[i + 1] + 1):
            allowed.add((r, c))

def valid_rectangle(p1, p2):
    r1, c1 = p1
    r2, c2 = p2

    top, bot = min(r1, r2), max(r1, r2)
    left, right = min(c1, c2), max(c1, c2)

    for r in range(top, bot + 1):
        for c in range(left, right + 1):
            if (r, c) not in allowed:
                return False
    return True

def cal_area(p1, p2):
    r1, c1 = p1
    r2, c2 = p2
    return abs(r1 - r2) * abs(c1 - c2)

res = -1
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
            continue

        if valid_rectangle(points[i], points[j]):
            area = cal_area(points[i], points[j])
            res = max(res, area)

print(res)
