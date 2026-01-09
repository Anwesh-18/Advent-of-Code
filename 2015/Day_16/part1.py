content = open("input.txt","r").read()
lines = content.split("\n")

aunt_list = {}
required = {'children': 3, 'cats': 7,'samoyeds': 2,'pomeranians': 3,'akitas': 0,'vizslas': 0,'goldfish': 5,'trees': 3,'cars': 2,'perfumes': 1}

for line in lines:
    line = line.split()
    name = (line[0]+line[1].rstrip(':'))
    id1 = line[2].rstrip(':')
    num1 = int(line[3].rstrip(','))
    id2 = line[4].rstrip(':')
    num2 = int(line[5].rstrip(','))
    id3 = line[6].rstrip(':')
    num3 = int(line[7])

    if name not in aunt_list:
        aunt_list[name] = {id1:num1,id2:num2,id3:num3}

correct_aunt = 0

for aunt in aunt_list:
    found = True
    for req in required:
        if req in aunt_list[aunt].keys():
            if aunt_list[aunt][req] != required[req]:
                found = False
                break

    if found:
        correct_aunt  = aunt
        break

print(correct_aunt)
