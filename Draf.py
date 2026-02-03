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


graph = [[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1]]

initial = [0, 1]

n = len(graph)
vis = [False] * n
for i in initial:
    vis[i] = True


def dfs(cur, path):
    path.append(cur)
    vis[cur] = True
    for i, j in enumerate(graph[cur]):
        if j == 1 and not vis[i]:
            dfs(i, path)


res = []
for i in range(n):
    if not vis[i]:
        path = []
        dfs(i, path)
        res.append(path[:])
# print(res)

# 源头-入口 so
so = defaultdict(list)

for i in initial:
    for idx, j in enumerate(graph[i]):
        if j == 1:
            so[i].append(idx)

res1 = defaultdict(list)
# 每个入口对应的源头 res1
for i, j in so.items():
    for k in j:
        if k != i:
            res1[k].append(i)
initial = set(initial)
# print(res1)

ans1 = Counter()

for i in res:
    cnt1 = set()
    for j in i:
        # print(res1[j])
        for k in res1[j]:
            if k in initial:
                cnt1.add(k)
    if len(cnt1) == 1:
        cnt1 = list(cnt1)
        ans1[cnt1[0]] += len(i)
ans1 = [[i, j] for i, j in ans1.items()]
ans1.sort(key=lambda x: (-x[1], x[0]))

# print(ans1)
if ans1:
    print(ans1[0][0])
else:
    print(min(initial))
