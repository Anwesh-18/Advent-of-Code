from collections import Counter

content = open('input.txt').read()
lines = content.split('\n')

def is_real(line,check_sum):
    to_check = ""
    line = "".join(line)
    count = Counter(line)

    sorted_letters = sorted(count.items(),key=lambda x:(-x[1],x[0]))
    for k,v in sorted_letters:
        to_check += k
    # print(to_check)
    if to_check[:5] == check_sum:
        return True
    else:
        return False

res = 0

for line in lines:
    line = line.split("-")
    sector_id = int(line[-1][:3])
    check_sum = line[-1][3:].strip("[]")
    if is_real(line[:-1],check_sum):
        # print(sector_id)
        res += sector_id

print(res)