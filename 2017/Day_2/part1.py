content = open("input.txt","r").read()
lines = content.split()

grps = []
nums = []
for line in lines:
    nums.append(int(line))
i=0
while i < len(nums):
    grps.append(nums[i:i+16])
    i+=16
# print(grps)

res = 0
for i in range(len(grps)):
    res += max(grps[i]) - min(grps[i])

print(res)