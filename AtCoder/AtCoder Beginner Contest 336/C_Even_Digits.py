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
    n = ii() - 1
    if n == 0:
        print(0)
        return
    nums = ["0", "2", "4", "6", "8"]
    ans = ""
    while n > 0:
        res = n % 5
        n = n // 5
        ans += nums[res]
    print(ans[::-1])


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
