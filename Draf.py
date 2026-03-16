import heapq
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt


n = 1
k = 4

tar = ['a', 'b', 'c']
res = [0]

def dfs(idx, cur):

    if len(cur) == n:
        res[0] = cur
        return
    for i in tar:
        if not cur or i != cur[-1]:
            cur.append(i)
            dfs(idx + 1, cur)
            cur.pop()

dfs(1, [])

print(res)
