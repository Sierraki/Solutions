import heapq
import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from math import floor, sqrt

input = sys.stdin.readline


def mii():
    return map(int, input().split())


def lmii():
    return list(mii())


def ii():
    return int(input())


size = ii()
for _ in range(size):
    n, m, h = mii()
    nums = lmii()
    tmp = nums.copy()
    vis = [0] * n
    cur = 0
    for _ in range(m):
        idx, val = mii()
        idx -= 1
        nums[idx] += val
        if vis[idx] != cur:
            nums[idx] = tmp[idx] + val
            vis[idx] = cur
        if nums[idx] > h:
            cur += 1
            nums[idx] = tmp[idx]
        vis[idx] = cur
    for i in range(n):
        if vis[i] != cur:
            nums[i] = tmp[i]
    print(*nums)
