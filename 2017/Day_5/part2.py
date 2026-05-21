content = open("input.txt","r").read()
nums = content.split("\n")
maze = []

for num in nums:
    maze.append(int(num))

idx=0
prev_idx=0
step = 0

while idx < len(maze):
    prev_idx = idx
    next_idx = idx + maze[idx]
    if maze[prev_idx] >= 3:
        maze[prev_idx] -= 1
    else:
        maze[prev_idx] += 1
    idx = next_idx
    step += 1

print(step)