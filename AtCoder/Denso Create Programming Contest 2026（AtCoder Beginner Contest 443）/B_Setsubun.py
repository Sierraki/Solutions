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
    n, k = mii()
    left = 0
    right = 10**8
    ans = right
    while left <= right:
        mid = (left + right) // 2
        cnt = mid + 1
        first = n
        last = n + mid
        res = cnt * (first + last) // 2
        if res >= k:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ans)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
