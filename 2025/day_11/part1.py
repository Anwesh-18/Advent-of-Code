content = open("input.txt").read().split('\n')

adj = {}
for line in content:
    key,val = line.split()[0].rstrip(':'),line.split()[1:]
    adj[key] = val

memo = {}

def dfs(node):
    if node in memo:
        return memo[node]
    
    count = 0
    for val in adj.get(node, []):
        if val == 'out':
            count += 1
        else:
            count += dfs(val)
    
    memo[node] = count
    return count

print(dfs('you'))