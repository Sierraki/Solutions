from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate
from functools import cache, lru_cache
import heapq
import copy


def p(numss):
    for i in numss:
        print(i)

colors = "bbbaaa"
neededTime = [4, 9, 3, 8, 8, 9]

n = len(colors)

res = []

pin = 0

for i, j in enumerate(colors):
    if j == colors[pin]:
        continue
    else:
        res.append(neededTime[pin:i])
        pin = i

if pin != n + 1:
    res.append(neededTime[pin:])


def fun(nums):
    total = sum(nums)
    ans = 0
    for i, j in enumerate(nums):
        if i % 2 == 0:
            ans += j
    return min(ans, total - ans)


# p(res)

ans = 0

for i in res:
    ans += fun(i)

print(res)
print(ans)
