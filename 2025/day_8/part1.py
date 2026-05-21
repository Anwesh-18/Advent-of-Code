from collections import defaultdict

content = open('input.txt', 'r').read()
lines = content.split('\n')

points = []
pairs = []

for line in lines:
    x,y,z = line.split(',')
    points.append([int(x),int(y),int(z)])

def cal_dist(point1,point2):
    x1,y1,z1 = point1
    x2,y2,z2 = point2
    return (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2

for i in range(len(points)):
    for j in range(i+1,len(points)):
        dist = cal_dist(points[i],points[j])
        pairs.append((dist,i,j))

pairs.sort()

parent = list(range(len(points)))
size = [1] * len(points)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

K = 1000

for k in range(min(K, len(pairs))):
    _, i, j = pairs[k]
    union(i, j)

components = defaultdict(int)

for i in range(len(points)):
    root = find(i)
    components[root] += 1

sizes = sorted(components.values(), reverse=True)
result = sizes[0] * sizes[1] * sizes[2]

print(result)