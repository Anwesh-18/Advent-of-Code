content = open('input.txt','r').read()
ids = content.split(',')

def is_invalid(num) -> bool:
    s = str(num)
    n = len(s)
    for d in range(1, n // 2 + 1):
        if n % d == 0:
            prefix = s[:d]
            if prefix * (n // d) == s:
                return True
    return False

total = 0

for id in ids:
    start, end = map(int, id.split('-'))
    for num in range(start, end + 1):
        if is_invalid(num):
            total += num

print(total)