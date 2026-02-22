import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from itertools import accumulate
from math import floor, sqrt

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
nums = deque(lmii())
res = 0
cnt = 1
while cnt >= 1 and nums:
    cnt -= 1
    cur = nums.popleft()
    cnt = max(cnt, cur - 1)
    res+=1
print(res)
