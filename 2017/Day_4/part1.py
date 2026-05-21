content = open("input.txt","r").read()
lines = content.split("\n")



def is_valid(line):
    seen = set()
    words = line.split()
    for word in words:
        if word not in seen:
            seen.add(word)
        else:
            return False
    return True

count = 0
for line in lines:
    if is_valid(line):
        count += 1

print(count)