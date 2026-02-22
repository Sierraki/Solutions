import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

input = sys.stdin.readline


def p(nums):
    for i in nums:
        print(i)


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
    n, m, l, s, t = mii()
    nums = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, c = mii()
        nums[u].append([v, c])
    res = set()

    def dfs(cur, path, cost):
        if path > l or cost > t:
            return
        if (path) == l and s <= cost <= t:
            res.add(cur)
            return
        for i, j in nums[cur]:
            dfs(i, path + 1, cost + j)

    dfs(1, 0, 0)
    print(*sorted(list(res)))


sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
