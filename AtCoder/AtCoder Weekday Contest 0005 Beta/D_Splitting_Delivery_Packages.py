import heapq
import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
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


def ms(numss):
    return "".join(map(str, numss))


def solve():
    n, k = mii()
    nums = lmii()

    def check(nums, tar, le):
        cur = 0
        res = 0
        for i in nums:
            cur += i
            if cur >= tar:
                res += 1
                cur = 0
        return res >= le
    left, right = 0, sum(nums) + 1
    ans = 0
    while left < right:
        # [)
        mid = (left + right) // 2
        if check(nums, mid, k):
            left = mid + 1
            ans = mid
        else:
            right = mid
    print(ans)
    pass


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
