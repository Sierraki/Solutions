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


def lacc(nums):
    return list(accumulate(nums))


n = ii()
nums = lmii()
pf = lacc(nums)
res = []
cnt = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        ans = pf[j - 1]
        if i != 0:
            ans -= pf[i - 1]
        swap = True
        for k in range(i, j):
            if ans % nums[k] == 0:
                swap = False
                break
        if swap == True:
            cnt += 1
print(cnt)
