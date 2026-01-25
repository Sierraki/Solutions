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
    has = [False] * (n + 1)
    for x in nums:
        dp[x] = 1
        has[x] = True
    for i in range(1, n + 1):
        if dp[i] != float("inf"):
            for j in range(2 * i, n + 1, i):
                mult = j // i
                if has[mult]:
                    if dp[i] + 1 < dp[j]:
                        dp[j] = dp[i] + 1
    ans = []
    for i in range(1, n + 1):
        if dp[i] == float("inf"):
            ans.append(-1)
        else:
            ans.append(dp[i])
    print(*ans)

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
