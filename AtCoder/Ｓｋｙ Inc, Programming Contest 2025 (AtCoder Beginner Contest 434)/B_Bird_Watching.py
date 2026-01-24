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


n, m = mii()
cnt = defaultdict(list)
for i in range(1, m + 1):
    cnt[i] = []
for _ in range(n):
    a, b = mii()
    cnt[a].append(b)
for i in cnt.values():
    print(sum(i) / len(i))
