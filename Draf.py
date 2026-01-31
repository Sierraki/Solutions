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


n, m = mii()
ma = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = mii()
    ma[a][b] = 1
p(ma)

res = []
path = []

start = 1
end = 5


def dfs(cur, path):
    if cur == end:
        res.append(path.copy())
        return
    if not path:
        path.append(cur)
    # 对cur行进行遍历
    for idx, i in enumerate(ma[cur]):
        if i == 1:
            path.append(idx)
            dfs(idx, path)
            path.pop()


dfs(1, [])
print(res)
