content = open("input.txt","r").read()
lines = content.split("\n")

towns = []
connections = {}

for line in lines:
    u,_,v,_,w = line.split()
    w = int(w)

    connections.setdefault(u,[]).append((v,w))
    connections.setdefault(v,[]).append((u,w))

max_dist = 0

def dfs(city, visited, total_cost):
    global max_dist

    if len(visited) == len(connections):
        max_dist = max(max_dist, total_cost)
        return

    for neighbour,cost in connections[city]:
        if neighbour not in visited:
            visited.add(neighbour)
            dfs(neighbour, visited, total_cost + cost)
            visited.remove(neighbour)

for start in connections:
    dfs(start,{start},0)

print(max_dist)