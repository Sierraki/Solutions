from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd
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
    w, h, d = mii()
    n = ii()
    
    a = gcd(n, w)
    n //= a
    b = gcd(n, h)
    n //= b
    c = n
    if d % c == 0:
        print(a - 1, b - 1, c - 1)
    else:
        print(-1)


sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    #     solve()
    solve()
