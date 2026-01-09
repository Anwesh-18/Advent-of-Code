import itertools

content = open("input.txt","r").read().strip()
lines = content.split(".\n")

people = []
happiness = {}

for line in lines:
    line = line.rstrip('.').split()
    if line[0] not in people:
        people.append(line[0])

    if (line[0],line[10]) not in happiness:
        if line[2] == 'gain':
            happiness[(line[0],line[10])] = int(line[3])
        else:
            happiness[(line[0],line[10])] = 0 - int(line[3])

first = people[0]
combs = itertools.permutations(people[1:])
# print(combs)
total_happiness = 0

def calc_happiness(comb,happiness):
    curr_happiness = 0
    for i in range(len(comb)):
        right = happiness[(comb[i],comb[(i+1)%len(comb)])]
        left = happiness[(comb[i], comb[(i-1) % len(comb)])]

        curr_happiness += right + left

    return curr_happiness

for comb in combs:
    comb = (first,) + comb
    total_happiness = max(total_happiness, calc_happiness(comb,happiness))

print(total_happiness)