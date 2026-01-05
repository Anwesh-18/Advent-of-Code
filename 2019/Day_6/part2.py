content = open("input2.txt").read().strip().split("\n")

parent = {}
for line in content:
    a, b = line.split(")")
    parent[b] = a

you_path = []
curr = parent["YOU"]
while curr != "COM":
    you_path.append(curr)
    curr = parent[curr]
you_path.append("COM")

san_path = []
curr = parent["SAN"]
while curr != "COM":
    san_path.append(curr)
    curr = parent[curr]
san_path.append("COM")

min_dist = float("inf")

for obj in you_path:
    if obj in san_path:
        dist = you_path.index(obj) + san_path.index(obj)
        min_dist = min(min_dist, dist)
print(min_dist)
