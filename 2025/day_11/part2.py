content = open("input.txt").read().split('\n')

adj = {}
for line in content:
    if not line.strip():
        continue
    parts = line.split()
    key = parts[0].rstrip(':')
    adj[key] = parts[1:]


memo = {}
def dfs(node, has_dac, has_fft):

    if node == 'dac':
        has_dac = True
    if node == 'fft':
        has_fft = True

    state = (node, has_dac, has_fft)

    if state in memo:
        return memo[state]

    if node == 'out':
        return 1 if (has_dac and has_fft) else 0

    total = 0
    for nei in adj.get(node, []):
        total += dfs(nei, has_dac, has_fft)
    
    memo[state] = total
    return total


print(dfs('svr', False, False))