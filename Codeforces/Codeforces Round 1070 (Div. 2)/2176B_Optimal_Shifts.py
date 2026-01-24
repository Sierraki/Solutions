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
    n = ii()
    s = si()
    m0 = m1 = c0 = c1 = 0
    for i in s + s:
        if i == "1":
            c0 = 0
            c1 += 1
            m1 = max(c1, m1)
        else:
            c1 = 0
            c0 += 1
            m0 = max(c0, m0)
    print(m0)
