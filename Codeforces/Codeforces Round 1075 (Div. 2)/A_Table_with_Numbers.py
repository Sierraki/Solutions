from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate
import sys

input = sys.stdin.readline


def mii():
    return map(int, input().split())


def lmii():
    return list(map(int, input().split()))


def ii():
    return int(input())


def si():
    return input()[:-1]


size = ii()
for _ in range(size):
    n, h, l = mii()
    nums = lmii()
    r = c = both = 0
    for i in nums:
        if 0 <= i - 1 < h and 0 <= i - 1 < l:
            both += 1
        elif 0 <= i - 1 < h:
            r += 1
        elif 0 <= i - 1 < l:
            c += 1
    dif = abs(r - c)
    ans = min(r, c)
    if dif > both:
        cur = both
    elif dif < both:
        cur = dif + (both - dif) // 2
    else:
        cur = dif
    ans += cur
    print(ans)
