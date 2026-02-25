import heapq
import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt
input = sys.stdin.readline
# num
def ii(): return int(input())
def mii(): return map(int, input().split())
def lmii(): return list(map(int, input().split()))
# string
def lmsi(): return list(map(str, si()))
def si(): return input().strip()
def ms(numss): return "".join(map(str, numss))
# else
def lacc(nums): return list(acc(nums))
def matt(row, col): return [[0] * col for _ in range(row)]
def p(numss):
    for i in numss:
        print(i)
def read_mat(n): return [lmii() for _ in range(n)]

def solve():
    s, m = mii()
    low = m & -m
    # print(low)
    if s % low != 0:
        print(-1)
    else:
        bit = []
        for j in range(60, -1, -1):
            if (m >> j) & 1:
                bit.append(1 << j)
        # print(bit)
        def check(n):
            rem = s
            for val in bit:
                take = min(n, rem // val)
                rem -= take * val
            return rem == 0
        low = 1
        high = s // low
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        print(ans)
    pass

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
