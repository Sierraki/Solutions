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


def ms(numss):
    return "".join(map(str, numss))


def solve():
    n = ii()
    p = lmii()
    a = lmii()
    cnt = Counter()
    for i, j in enumerate(p):
        cnt[j] = i
    res = [cnt[a[0]]]
    for i in range(1, n):
        if a[i - 1] == a[i]:
            continue
        else:
            res.append(cnt[a[i]])
    swap = True
    for i in range(1, len(res)):
        if res[i - 1] <= res[i]:
            continue
        else:
            swap = False
            break
    print("YES" if swap else "NO")


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
