import math

content = open('input.txt', 'r').read().strip()
lines = content.split('\n')

points = []
for line in lines:
    x, y = line.split(',')
    points.append((int(y), int(x)))

def cal_area(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    return (abs(x1-x2) + 1) * (abs(y1-y2) + 1)

res = -1
for i in range(len(points)):
    for j in range(i+1,len(points)):
        area = cal_area(points[i],points[j])
        res = max(res,area)

print(res)