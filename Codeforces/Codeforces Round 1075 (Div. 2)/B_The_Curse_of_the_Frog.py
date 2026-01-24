from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate
import sys

# 设定输入
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
    n, x = mii()

    total = 0
    mx = -float("inf")

    for _ in range(n):
        a, b, c = mii()
        total += a * (b - 1)

        cur = a * b - c
        if cur > mx:
            mx = cur

    if total >= x:
        print(0)
    elif mx <= 0:
        print("-1")
    else:
        res = x - total
        ans = (res + mx - 1) // mx
        print(ans)
