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


n = ii()
nums = [["x"] * n for _ in range(n)]
nums[0][(n - 1) // 2] = 1
r, c, k = 0, (n - 1) // 2, 1
for _ in range(n**2 - 1):
    if nums[(r - 1) % n][(c + 1) % n] == "x":
        nums[(r - 1) % n][(c + 1) % n] = k + 1
        r, c = (r - 1) % n, (c + 1) % n
    else:
        nums[(r + 1) % n][c] = k + 1
        r = (r + 1) % n
    k += 1
for i in nums:
    print(*i)
