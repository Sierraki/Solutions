import heapq
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt
from operator import ne

from matplotlib.pyplot import flag


def p(numss):
    for i in numss:
        print(i)

energy = [5, -10, 4, 3, 5, -9, 9, -7]
k = 2

dp = [0] * len(energy)
ans = -float('inf')
for i, j in enumerate(energy):
    if i - k >= 0:
        dp[i] = max(j, j + dp[i - k])
        ans=max()

    else:
        dp[i] = j

print(dp)
print(dp[-1])
