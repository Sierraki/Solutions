import heapq
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

def p(numss):
    for i in numss:
        print(i)



nums = [[4, 1, 2, 3, 4],
        [3, 2, 5, 6],
        [2, 1, 3],
        [3, 4, 7, 8],
        [2, 6, 8],
        [0],
        ]

m = 8
n = len(nums)

check = [set(i) for i in nums]
p(check)

vis = [True] + [False] * (m)
res = [0]
def dfs(cur, path):
    if cur == n:
        if len(path) > res[0]:
            res[0] = len(path)
        return

    for i in check[cur]:
        if vis[i] == False:
            vis[i] = True
            path.append(i)
            dfs(cur + 1, path)
            path.pop()
            vis[i] = False
    else:
        dfs(cur + 1, path)

dfs(0, [])

print(bin(5), bin(4))
