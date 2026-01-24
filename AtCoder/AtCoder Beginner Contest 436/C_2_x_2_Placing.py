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
cnt = defaultdict(set)
ans = 0


def fun(a, b):
    cell = [[a, b], [a - 1, b], [a, b - 1], [a - 1, b - 1]]
    swap = True
    if (0 <= a - 1 < n and 0 <= b - 1 < n) and (0 <= a < n and 0 <= b < n):
        for i, j in cell:
            if j in cnt[i]:
                swap = False
    if swap == True:
        for i, j in cell:
            cnt[i].add(j)
        return 1
    return 0


for _ in range(m):
    a, b = mii()
    ans += fun(a, b)
# print(cnt)
print(ans)
