import heapq
import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

input = sys.stdin.readline


# num
def ii(): return int(input())
def mii(): return map(int, input().split())
def lmii(): return list(map(int, input().split()))
# string
def lmsi(): return list(map(str, si()))
def si(): return input().strip()
def ms(numss): return "".join(map(str, numss))
# else
def lacc(nums): return list(acc(nums))
def matt(row, col): return [[0] * col for _ in range(row)]
def p(numss):
    for i in numss:
        print(i)
def read_mat(n): return [lmii() for _ in range(n)]


def solve():
    n, m = mii()
    nums = read_mat(n)
    p(nums)
    check = [set(i) for i in nums]
    # p(check)

    vis = [True] + [False] * (m)
    res = [0]

    def dfs(cur, path):
        if cur == n:
            if len(path) > res[0]:
                res[0] = len(path)
            return

        for i in check[cur]:
            if vis[i] == False:
                vis[i] = True
                path.append(i)
                dfs(cur + 1, path)
                path.pop()
                vis[i] = False
        else:
            dfs(cur + 1, path)
    dfs(0, [])

    print(res[0])


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
