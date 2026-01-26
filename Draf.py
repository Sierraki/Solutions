from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate as acc
import heapq
import copy


def p(nums):
    for i in nums:
        print(i)


def lacc(nums):
    return list(acc(nums))


n = 8
nums = [3, 2, 2, 3, 7, 3, 6, 7]

dp = [float("inf")] * (n + 1)
vis = [False] * (n + 1)

for i in nums:
    vis[i] = True
    dp[i] = 1
    # print(i)

for i in range(1, n + 1):
    if dp[i] != float("inf"):
        for j in range(2 * i, n + 1, i):
            res = j // i
            dp[j] = min(dp[j], dp[res] + dp[i])

ans = [i if i!=float('inf') else -1 for i in  (dp[1:])]
print(list(range(n + 1)))
print(vis)
print(dp)

print(ans)
