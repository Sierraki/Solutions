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
nums = [lmii() for _ in range(m)]
cnt = defaultdict(set)
for i, j in nums:
    cnt[i].add(j)
    cnt[j].add(i)
dp = [0] * (n + 1)
for i in range(1, n + 1):
    cur = n - len(cnt[i]) - 1
    if cur >= 3:
        dp[i] = cur * (cur - 1) * (cur - 2) // 6
    else:
        dp[i] = 0
print(*dp[1:])
