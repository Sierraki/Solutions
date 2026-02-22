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
    n=ii()
    s=si()
    idx1 = [i + 1 for i, j in enumerate(s) if j == '1']
    idx0 = [i + 1 for i, j in enumerate(s) if j == '0']
    if len(idx1) % 2 == 0:
        print(len(idx1))
        if not idx1:
            pass
        else:
            print(*idx1)
    elif len(idx0) % 2 != 0:
        print(len(idx0))
        if not idx0:
            pass
        else:
            print(*idx0)
    else:
        print(-1)

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
