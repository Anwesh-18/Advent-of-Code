content = open("input.txt","r").read()
target = int(content)

limit = target // 11

houses = [0]*(limit+1)

for elf in range(1,limit+1):
    for k in range(1,51):
        house = elf * k
        if house > limit:
            break
        houses[house] += elf*11

for i in range(1,limit+1):
    if houses[i] >= target:
        print(i)
        break
