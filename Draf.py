from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


grid = [[3, 2], [1, 3], [3, 4], [0, 1]]

n = len(grid)
m = len(grid[0])

res = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        res[i][j] = grid[j][i]
ans = 0
for i in res:
    for j in range(1, n):
        if i[j] <= i[j - 1]:
            ans += i[j - 1] - i[j] + 1
            i[j] = i[j - 1] + 1
print(res, ans)
