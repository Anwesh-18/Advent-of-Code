content = open('input.txt','r').read()
lines = content.split('\n')

def is_triangle(line):
    a,b,c = map(int,line.split())
    if a+b > c and a+c > b and b+c > a :
        return True
    else:
        return False

count = 0
for line in lines:
    if is_triangle(line):
        count += 1

print(count)