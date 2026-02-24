import heapq
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

def p(numss):
    for i in numss:
        print(i)

nums = [1, 1, 1, 1]
target = -1000

total = sum(nums)

po = (total + target) / 2

print(po)
n = len(nums)
if po % 1 == 0:
    po = int(po)
    dp = [[0] * (po + 1) for _ in range(n)]

    dp[0][0] = 1
    if nums[0] <= po:
        dp[0][nums[0]] += 1

    for i in range(1, n):
        for j in range(po + 1):
            # 选
            dp[i][j] = dp[i - 1][j]
            # 不选
            if j >= nums[i]:
                dp[i][j] += dp[i - 1][j - nums[i]]
    print(dp[-1][-1])




else:
    print(0)


p(dp)
