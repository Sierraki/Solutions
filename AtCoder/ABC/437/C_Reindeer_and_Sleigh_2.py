from collections import defaultdict as dfd, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate as acc
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
    nums = [lmii() for _ in range(n)]
    total = sum([i[0] for i in nums])
    tar = [i + j for i, j in nums]
    tar.sort(reverse=True)
    pf = list(acc(tar))
    tar = bisect_left(pf, total) + 1
    print(n - tar)
