from collections import defaultdict, Counter, deque
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


def lacc(nums):
    return list(acc(nums))


n, m = mii()
nums = []
for _ in range(m):
    nums.append(lmii())
de = [0] * (n + 1)
for i, j in nums:
    de[i] += 1
    de[j] += 1
res = []
for i in range(1, n + 1):
    k = n - 1 - de[i]
    if k < 3:
        res.append(0)
    else:
        val = k * (k - 1) * (k - 2) // 6
        res.append(val)
print(*res)
