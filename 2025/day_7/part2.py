content = open('input.txt', 'r').read()
lines = content.split('\n')

grid = []
count = 0

for line in lines:
    temp = []
    for ch in line:
        temp.append(ch)
    grid.append(temp)

grid[1][7] = "|"

for i in range(len(grid)):
    print("".join(grid[i]))


def count_paths(grid):
    memo = {}

    def dp(r, c):
        # If past bottom, reached end
        if r == len(grid):
            return 1
        if (r, c) in memo:
            return memo[(r, c)]

        if grid[r][c] == '^':
            total = dp(r + 1, c - 1) + dp(r + 1, c + 1)
        else:
            total = dp(r + 1, c)

        memo[(r, c)] = total
        return total

    start_col = grid[0].index('S')
    return dp(1, start_col)

print(count_paths(grid))