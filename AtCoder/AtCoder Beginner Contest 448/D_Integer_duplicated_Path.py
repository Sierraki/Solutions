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
    n = ii()
    nums = [0] + lmii()
    adj = [[]for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = mii()
        adj[a].append(b)
        adj[b].append(a)
    res = ['No'] * (n + 1)
    vis = [False] * (n + 1)

    def dfs(cur, path, lv):
        if not vis[cur]:
            path[nums[cur]] += 1
            vis[cur] = True
            if len(path) != lv:
                res[cur] = 'Yes'
            for i in adj[cur]:
                dfs(i, path, lv + 1)
            lv -= 1
            path[nums[cur]] -= 1
            if path[nums[cur]] == 0:
                del path[nums[cur]]
            vis[cur] = False
    dfs(1, Counter(), 1)
    for i in res[1:]:
        print(i)
    pass

sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
