from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
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
    nums = lmii()
    p1 = [[nums[i], 0, i] for i in range(n) if i % 2 == 0]
    p2 = [[nums[i], 1, i] for i in range(n) if i % 2 == 1]
    res = p1 + p2
    res.sort(key=lambda x: x[0])
    ans=([i[1] for i in res])
    for i in range(1,n):
        if ans[i]==ans[i-1]:
            print('no')
            break
    else:
        print('yes')