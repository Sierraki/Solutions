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

bombs = [[2, 1, 3], [6, 1, 4]]

n = len(bombs)


def check(x1, y1, r1, x2, y2):
    return sqrt((y1 - y2) ** 2 + (x1 - x2) ** 2) <= r1


res = []

for i in range(n):
    for j in range(i + 1, n):
        a = bombs[i]
        b = bombs[j]
        if check(a[0], a[1], a[2], b[0], b[1]):
            res.append([i, j])
        if check(b[0], b[1], b[2], a[0], a[1]):
            res.append([j, i])
print(res)
adj = [[] for _ in range(n)]
for i, j in res:
    adj[i].append(j)

p(adj)
ans = []

vis = [False] * n


def dfs(cur, path):
    path.append(cur)
    vis[cur] = True
    for i in adj[cur]:
        if not vis[i]:
            dfs(i, path)


for i in range(n):
    path = []
    vis = [False] * n
    dfs(i, path)
    ans.append(path[:])

print(ans)

mx = -float("inf")
for i in ans:
    mx = max(mx, len(i))
print(mx)
