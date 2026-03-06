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


s = "10001100101000000"

s = list(map(int, s + s))



nums = [1 if i % 2 == j else 0 for i, j in enumerate(s)]


cur = 0
l = 0
k = len(s) // 2
ans = float('inf')
for r, val in enumerate(nums):
    if r < k:
        cur += val
    else:
        cur += val
        cur -= nums[l]
        l += 1
        ans = min(ans, cur, k - cur)


print(ans)
