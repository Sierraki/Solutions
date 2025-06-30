from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

m = len(grid)
n = len(grid[0])
nums = [j for i in grid for j in i]
dp = [0] * m * n
s = 0
for i in range((m * n)):
    if i < n:
        s += nums[i]
        dp[i] = s
    elif i > 0 and i % n == 0:
        dp[i] = nums[i] + dp[i - n]
    else:
        dp[i] = min(dp[i - n], dp[i - 1]) + nums[i]
print(dp)
