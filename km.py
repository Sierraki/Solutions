from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate as acc
import sys

input = sys.stdin.readline


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


def solve():
    n, m = mii()
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = mii()
        adj[a].append(b)
    res = []

    def dfs(cur, path):

        path.append(cur)
        if cur == n:

            res.append(path[:])
        else:
            for i in adj[cur]:

                dfs(i, path)
        path.pop()

    dfs(1, [])
    for i in res:
        print(*i)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
