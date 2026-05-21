content = open('input.txt','r').read()
ids = content.split(',')

def is_invalid(n):
    s = str(n)
    if len(s)%2 != 0:
        return False
    half = len(s)//2
    return s[:half] == s[half:]

total = 0

for id in ids:
    start, end = map(int, id.split('-'))
    for i in range(start, end + 1):
        if is_invalid(i):
            total += i

print(total)