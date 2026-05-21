from itertools import combinations, permutations

content = open("input.txt","r").read()
lines = content.split("\n")



def is_valid(line):
    seen = set()
    words = line.split()
    for word in words:
        el = "".join(sorted(word))
        if el in seen:
            return False
        seen.add(el)
    return True

count = 0
for line in lines:
    if is_valid(line):
        count += 1

print(count)