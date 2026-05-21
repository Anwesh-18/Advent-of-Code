content = open('input.txt','r').read()
lines = content.split('\n')

ranges = []
next_iter = False
valid = 0

def check_num(num,nums):
    for rg in nums:
        if rg[0]<= num <= rg[1]:
            return True

    return False


for line in lines:
    if line.strip() == "":
        next_iter = True
        continue

    if not next_iter:
        start,end = line.split('-')
        ranges.append((int(start),int(end)))

    else:
        if check_num(int(line),ranges):
            valid += 1

print(valid)