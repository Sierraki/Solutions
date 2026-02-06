from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
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
    n, x, y = mii()
    nums = lmii()

    def fun(x, y, total, ai):
        return (total - x * ai) // (y - x)

    diff = y - x
    res = (nums[0] * x) % diff
    for i in nums:
        if (i * x) % diff != res:
            print(-1)
            return
    if max(nums) * x > min(nums) * y:
        print(-1)
        return
    cnt = 0
    tar = min(nums) * y
    for i in nums:
        cnt += fun(x, y, tar, i)
    print(cnt)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
