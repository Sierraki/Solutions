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


n = 7
edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]

nums = [[] for _ in range(n)]
for i, j in edges:
    nums[i].append(j)
    nums[j].append(i)


vis = [False] * n

res = []


def dfs(cur, path):
    vis[cur] = True
    path.append(cur)
    for i in nums[cur]:
        if not vis[i]:
            dfs(i, path)


for i in range(n):
    if not vis[i]:
        path = []
        dfs(i, path)
        res.append(len(path))
print(res)
ans = 0

total = sum(res)

for i in res:
    total -= i
    ans += i * total

print(ans)
print(nums)
