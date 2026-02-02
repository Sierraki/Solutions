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


n = 4
k = 1
invocations = [[1, 2], [0, 1], [3, 2]]

nums = [[] for _ in range(n)]
for i, j in invocations:
    nums[i].append(j)


vis = [False] * n

res = set()


def dfs(cur):
    if not vis[cur]:
        vis[cur] = True
        res.add(cur)
        for i in nums[cur]:
            if not vis[i]:
                dfs(i)


dfs(k)

# 可疑节点 res
