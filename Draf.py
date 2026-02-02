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


n = 6
connections = [[0, 1], [0, 2], [0, 3], [1, 2]]

cable = len(connections)

nums = [[] for _ in range(n)]
for i, j in connections:
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
        res.append((path[:]))

print(res)
need = len(res) - 1
cur=0
for i in res:
    cur+=len(i)-1
print(need)
print(cable)

if len(res)==1:
    ans=0
elif need+cur>cable:
    ans=-1
else:
    ans=cur

print(ans)