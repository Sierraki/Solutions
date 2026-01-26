from collections import defaultdict, Counter, deque
from math import sqrt, floor,gcd
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
    n=ii()
    nums=lmii()
    dp = [float("inf")] * (n + 1)
    vis = [False] * (n + 1)
    for i in nums:
        vis[i] = True
        dp[i] = 1
    for i in range(1, n + 1):
        if dp[i] != float("inf"):
            for j in range(2 * i, n + 1, i):
                res = j // i
                dp[j] = min(dp[j], dp[res] + dp[i])
    ans = [i if i != float("inf") else -1 for i in (dp[1:])]
    print(*ans)

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
