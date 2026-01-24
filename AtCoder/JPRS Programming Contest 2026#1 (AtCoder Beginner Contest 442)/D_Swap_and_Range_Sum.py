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


n, q = mii()
nums = lmii()
pf = [0] + lacc(nums)
nums = [0] + nums
for _ in range(q):
    cur = lmii()
    if cur[0] == 1:
        x = cur[1]
        pf[x] = pf[x] - nums[x] + nums[x + 1]
        nums[x], nums[x + 1] = nums[x + 1], nums[x]
    elif cur[0] == 2:
        l, r = cur[1], cur[2]
        print(pf[r] - pf[l - 1])
