content = open("input.txt","r").read()
lines = content.split("\n")

deer_data = {}
dist = {}
time_left = {}
time_flew = {}
points = {}

for line in lines:
    line = line.rstrip('.').split()
    deer = line[0]
    speed = int(line[3])
    time = int(line[6])
    rest = int(line[13])
    if deer not in deer_data:
        deer_data[deer] = (speed, time, rest)
    if deer not in dist:
        dist[deer] = 0
    if deer not in time_left:
        time_left[deer] = 0
    if deer not in time_flew:
        time_flew[deer] = 0
    if deer not in points:
        points[deer] = 0

for i in range(2503):
    for deer in deer_data:
        if time_left[deer] == 0:
            dist[deer] += deer_data[deer][0]
            time_flew[deer] += 1
            if time_flew[deer] >= deer_data[deer][1]:
                time_flew[deer] = 0
                time_left[deer] = deer_data[deer][2]
        else:
            time_left[deer] -= 1
    curr_dist = 0
    for deer,distance in dist.items():
        if curr_dist < distance:
            curr_dist = distance
    for deer in dist:
        if dist[deer] == curr_dist:
            points[deer] += 1

winner = 0
for deer,points in points.items():
    winner = max(winner,points)

print(winner)
