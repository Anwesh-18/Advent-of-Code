content = open("input.txt","r").read()
nums = content.split("\t")

seen = set()
seq = []

for num in nums:
    seq.append(int(num))

steps = 0
loop_found = False
while not loop_found:
    max_val = max(seq)
    idx = seq.index(max_val)
    to_give= max_val//(len(seq)-1)
    blocks = seq[idx]
    seq[idx] = 0

    i = idx + 1
    while blocks > 0:
        seq[i % len(seq)] += 1
        blocks -= 1
        i += 1
        steps += 1
    sequence = tuple(seq)
    if sequence not in seen:
        seen.add(sequence)
    else:
        loop_found = True

print(steps)