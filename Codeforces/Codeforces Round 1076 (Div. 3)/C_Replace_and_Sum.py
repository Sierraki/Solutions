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
    n, q = mii()
    a = lmii()
    b = lmii()
    pin = n - 1
    while pin >= 0:
        if pin == n - 1:
            a[pin] = max(a[pin], b[pin])
        else:
            a[pin] = max(a[pin], a[pin + 1], b[pin])
        pin -= 1
        if pin < 0:
            break
    pf = [0] + lacc(a)
    res=[]
    for _ in range(q):
        l, r = mii()
        res.append(pf[r] - pf[l - 1])
    print(*res)

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
