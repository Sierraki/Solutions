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
    x, y, z = mii()
    if x // y == z and x % y == 0:
        print("Yes")
    else:
        if (x - z * y) % (z - 1) == 0 and (x - z * y)// (z - 1)>=0:
            print("Yes")
        else:
            print("No")


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
