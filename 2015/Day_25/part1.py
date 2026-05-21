content = open("input.txt","r").read().split()
row = int(content[15].rstrip(','))
col = int(content[17].rstrip('.'))

n = row + col - 1
prev = 20151125
for i in range(2,n+1):
    found = False
    start = i
    end = 1
    while start >= 1:
        mul = prev*252533
        rem = mul % 33554393
        prev = rem
        if start == row and end == col:
            found = True
            break
        start -= 1
        end += 1

    if found:
        break

print(prev)