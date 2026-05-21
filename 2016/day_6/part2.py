from collections import Counter

content = open('input.txt').read()
lines = content.split('\n')

res = [[] for _ in range(len(lines[0]))]

for line in lines:
    idx = 0
    for ch in line:
        res[idx].append(ch)
        idx += 1

ans = ""
for part in res:
    count = Counter(part)
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    ans += sorted_count[-1][0]

print(ans)