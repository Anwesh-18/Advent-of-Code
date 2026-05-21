content = open('input.txt','r').read()
lines = content.split('\n')

def is_triangle(a,b,c):
    if a+b > c and a+c > b and b+c > a :
        return True
    else:
        return False

count = 0
sides = []
t = 1

for line in lines:
    a,b,c = map(int,line.split())
    sides.append([a,b,c])

for i in range(3):
    it = 1
    test = []
    for j in range(len(sides)):
        test.append(sides[j][i])
        if it%3==0:
            if is_triangle(test[0],test[1],test[2]):
                count += 1
            test.clear()
        it+=1

print(count)
