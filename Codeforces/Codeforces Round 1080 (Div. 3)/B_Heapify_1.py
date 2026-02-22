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

def fun(n):
    while n % 2 == 0:
        n //= 2
    return n
def solve():
    n = ii()
    nums = lmii()
    for i in range(n):
        idx = i + 1
        if fun(nums[i]) != fun(idx):
            print("NO")
            break
    else:
        print("YES")

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
