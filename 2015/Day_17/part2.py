from itertools import combinations

content = open("input.txt","r").read()
nums = content.split("\n")

my_list = []

for num in nums:
    my_list.append(int(num))

min_cont = float("inf")

for r in range(1,len(my_list)+1):
    for combo in combinations(my_list,r):
        if sum(combo) == 150:
            min_cont = min(min_cont,len(combo))

count = 0
for combo in combinations(my_list,min_cont):
    if sum(combo) == 150:
        count += 1

print(count)