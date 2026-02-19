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

    res = [0] * n
    for i in range(1, n - 1):
        res[i] = (nums[i + 1] - 2 * nums[i] + nums[i - 1]) // 2
    # last
    last = 0
    # print(res)
    for i in range(1, n - 1):
        last += i * res[i]
    # mid
    res[n - 1] = (nums[0] - last) // (n - 1)
    # print(res)
    fn = 0
    for i in range(1, n - 1):
        fn += (n - 1 - i) * res[i]
        # print(fn)
    res[0] = (nums[n - 1] - fn) // (n - 1)

    print(*res)

    pass


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
