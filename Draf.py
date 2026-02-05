from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate as acc


grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1],
]

m = len(grid)
n = len(grid[0])

fresh = 0
tar = [[0, 1], [1, 0], [-1, 0], [0, -1]]
# 目标感染数量
total = sum([1 for i in grid for j in i if j >= 1])

nums = deque([])
for i in range(m):
    for j in range(n):
        if grid[i][j] == 2:
            nums.append([i, j])
        if grid[i][j] == 1:
            fresh += 1
# 起始一共有多少个烂的
rot = len(nums)
cnt = 0
while nums and fresh > 0:
    size = len(nums)
    for _ in range(size):
        x, y = nums.popleft()
        if grid[x][y] == 2:
            for i, j in tar:
                if 0 <= x + i < m and 0 <= y + j < n:
                    if grid[x + i][y + j] == 1:
                        nums.append([x + i, y + j])
                        grid[x + i][y + j] = 2
                        rot += 1
    cnt += 1
    if rot >= total:
        break
print(cnt)
