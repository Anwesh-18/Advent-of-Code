from itertools import combinations
from math import prod

content = open("input.txt","r").read()
numbers = content.split("\n")

nums = []
total = 0
for num in numbers:
    nums.append(int(num))
    total += int(num)

grps = []
target = total//3

best_qe = float("inf")

for r in range(1,len(nums)):
    found = False
    for combo in combinations(nums,r):
        if sum(combo) == target:
            found = True
            qe = prod(combo)
            best_qe = min(qe,best_qe)

        if found:
            break

print(best_qe)