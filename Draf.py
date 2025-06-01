from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

grid = [[1, -2, 3], [2, 3, 5]]
k = 2

m, n = len(grid), len(grid[0])
ans = []

for i in range(m - k + 1):
    row = []
    for j in range(n - k + 1):
        val = set()
        for x in range(i, i + k):
            for y in range(j, j + k):
                val.add(grid[x][y])
        if len(val) == 1:
            row.append(0)
        else:
            nums = sorted(val)
            mi = float("inf")
            for a in range(1, len(nums)):
                diff = nums[a] - nums[a - 1]
                if diff < mi:
                    mi = diff
            row.append(mi)
        print(mi)
    ans.append(row)
print(ans)
