import heapq
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

k = 3

res = []
swap = [True]

tar = ["01", "10"]

def dfs(cur):
    if swap[0]:
        if len(cur) == k or cur in tar:
            res.append(cur)
            swap[0] = False
            return
        dfs(cur + '1')
        dfs(cur + '0')
    else:
        return

dfs('')

print(res)
