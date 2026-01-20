from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate
import heapq
import copy
import sys


input = sys.stdin.readline


def mii():
    return map(int, input().split())


def lmii():
    return list(mii())


def ii():
    return int(input())


size = ii()
for _ in range(size):
    n, m, k = mii()
    rb = lmii()
    mo = lmii()
    s = input()[:-1]
    rb.sort()
    mo.sort()
    res = []
    cur = 0
    for i in s:
        if i == "L":
            cur -= 1
        else:
            cur += 1
        res.append(cur)
    left = [0] * k
    right = [0] * k
    left = list(accumulate([0] + res, min))
    right = list(accumulate([0] + res, max))
    del left[0]
    del right[0]
    for i in range(k):
        left[i] = abs(left[i])
    # 机器人位置
    mo = [-(20**18)] + mo + [20**18]
    ans = [n] * k
    of = [0] * k
    lcc = []
    for i in rb:
        l = abs(mo[bisect_left(mo, i) - 1] - i)
        r = mo[bisect_left(mo, i)] - i
        lc1 = bisect_left(left, l)
        lc2 = bisect_left(right, r)
        cur = min(lc1, lc2)
        if 0 <= cur < k:
            of[cur] -= 1
    of_pf = list(accumulate(of))
    for i in range(k):
        ans[i] += of_pf[i]
    print(*ans)
