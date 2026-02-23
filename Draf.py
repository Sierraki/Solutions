import heapq
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

def p(numss):
    for i in numss:
        print(i)

nums = [1]

target = 2


n = len(nums)
total = sum(nums)

if total < abs(target) or (total + target) % 2 != 0:
    print(0)

po = (total + target) // 2

dp = [[0] * (po + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, len(nums) + 1):
    num = nums[i - 1]
    for j in range(po + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= num:
            dp[i][j] += dp[i - 1][j - num]
p(dp)

print(dp[-1][-1])
