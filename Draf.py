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


graph = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
initial = [0, 2]

n = len(graph)
vis = [False] * n
initial = set(initial)

def dfs(cur, path):
    path.append(cur)
    vis[cur] = True
    for i, j in enumerate(graph[cur]):
        if j == 1:
            if not vis[i]:
                dfs(i, path)


res = []
for i in range(n):
    if not vis[i]:
        path = []
        dfs(i, path)
        res.append(path[:])
ans = []


def check(tar):
    res = []
    for i in tar:
        if i in initial:
            res.append(i)
    if len(res) > 1:
        return [[0, i] for i in res]
    elif len(res) == 1:
        return [[len(tar), res[0]]]
    return []


for i in res:
    cur = check(i)
    if cur:
        ans += cur


ans.sort(key=lambda x: (-x[0], x[1]))

print(res)
print(ans)
print(ans[0][1])
