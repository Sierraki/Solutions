from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate
from functools import cache
import heapq
import copy


def p(numss):
    for i in numss:
        print(i)


n = 3
k = 3

vis = [False] * (n)
res = []

swap = True


def dfs(path):
    global swap
    if swap:
        if len(path) == n:
            cur = "".join(path)
            res.append(cur)
            return
        if len(res) == k:
            swap = False
            return

        for i in range(n):
            if not vis[i]:
                path.append(str(i + 1))
                vis[i] = True
                dfs(path)
                path.pop()
                vis[i] = False
    return


dfs([])

print(res[-1])
