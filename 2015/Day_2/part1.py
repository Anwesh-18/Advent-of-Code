with open("input1.txt", "r") as f:
    lines = f.read().strip().splitlines()

sum = 0
for line in lines:
    l, w, h = map(int, line.split('x'))
    area = 2*((l*w)+(w*h)+(h*l))
    minArea = min((l*w),(w*h),(h*l))
    sum += area + minArea

print(sum)