from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate as acc
from functools import cache, lru_cache
import heapq
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
def ms(numss):
    return "".join(map(str, numss))
def solve():
    n = ii()
    nums = lmii()
    dp = [float("inf")] * 7
    for i in range(1, 7):
        if nums[0] == i:
            dp[i] = 0
        else:
            dp[i] = 1
    for i in nums[1:]:
        last = [float("inf")] * 7
        # print(last)
        for cur in range(1, 7):
            cost = 0 if i == cur else 1
            pre = float("inf")
            for j in range(1, 7):
                if j != cur and j + cur != 7:
                    if dp[j] < pre:
                        pre = dp[j]
            last[cur] = pre + cost
            # print(last,pre,cost)
        # print(dp)
        dp = last
    print(min(dp[1:]))
    pass

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
