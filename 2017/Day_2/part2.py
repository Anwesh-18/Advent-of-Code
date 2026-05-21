from itertools import combinations

content = open("input.txt", "r").read()
lines = content.split()

nums = [int(x) for x in lines]

grps = []
i = 0
while i < len(nums):
    grps.append(nums[i:i+16])
    i += 16

def evenly_divisible_value(nums):
    for a, b in combinations(nums, 2):
        if a % b == 0:
            return a // b
        if b % a == 0:
            return b // a

res = 0
for grp in grps:
    res += evenly_divisible_value(grp)

print(res)