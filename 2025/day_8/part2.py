content = open('input.txt', 'r').read()
lines = content.split('\n')

points = []
pairs = []

for line in lines:
    if not line.strip():
        continue
    x, y, z = line.split(',')
    points.append((int(x), int(y), int(z)))

def cal_dist(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2

n = len(points)

for i in range(n):
    for j in range(i + 1, n):
        dist = cal_dist(points[i], points[j])
        pairs.append((dist, i, j))

pairs.sort()

parent = list(range(n))
size = [1] * n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return True

components = n
last_pair = None

for _, i, j in pairs:
    if union(i, j):
        components -= 1
        last_pair = (i, j)
        if components == 1:
            break

i, j = last_pair
result = points[i][0] * points[j][0]
print(result)
