import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

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
    n = ii()
    nums = lmii()

    res = sorted(nums)
    if nums == res:
        print(-1)
    else:
        mi = res[0]
        mx = res[-1]
        ans = float("inf")
        for i in range(n):
            if nums[i] != res[i]:
                cur = max(nums[i] - mi, mx - nums[i])
                ans = min(ans, cur)
        print(ans)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
