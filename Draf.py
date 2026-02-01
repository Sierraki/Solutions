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


n = 5
edges = [[0, 4]]
source = 0
destination = 4

nums = [[] for _ in range(n)]
vis = [False] * n
for i, j in edges:
    nums[i].append(j)
    nums[j].append(i)
res = [False]
def dfs(cur):
    if cur == destination:
        res[0] = True
        return
    for i  in (nums[cur]):
        if vis[i] == False:
            vis[i] = True
            dfs(i)


vis[source] = True
dfs(source)
p(nums)
print(vis)

print(res[0])
