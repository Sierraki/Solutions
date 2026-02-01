from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate as acc
import heapq
import copy
import sys

input = sys.stdin.readline


def p(nums):
    for i in nums:
        print(i)


def lacc(nums):
    return list(acc(nums))


def mii():
    return map(int, input().split())


def lmii():
    return list(map(int, input().split()))


def ii():
    return int(input())


def si():
    return input().strip()


def lacc(nums):
    return list(acc(nums))


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

n = len(isConnected)
vis =  [False] * (n)


def dfs(cur):
    vis[cur ] = True
    for idx, j in enumerate(isConnected[cur ] ):
        if j == 1 and vis[idx] == False:
            vis[idx] = True
            dfs(idx)


cnt = 0
for i in range(n):
    if vis[i] == False:
        cnt += 1
        dfs(i)

print(cnt)
