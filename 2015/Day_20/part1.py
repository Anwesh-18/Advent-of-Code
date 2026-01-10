content = open("input.txt","r").read()
target = int(content)

def find_factors(n):
    res = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n // i)
        i += 1
    return res

i=1
while True:
    factors = find_factors(i)
    total_presents = 0
    for num in factors:
        total_presents += (num*10)

    if total_presents >= target:
        break

    i+=1

print(i)