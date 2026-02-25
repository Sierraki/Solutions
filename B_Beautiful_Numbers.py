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
    s = si()
    total = sum(int(i) for i in s)
    # print(total)
    if total <= 9:
        print(0)
    else:
        p1 = s[0]
        p2 = s[1:]
        # print(total)
        # print(nums)
        ans = 0
        res = []
        if int(p1) > 1:
            res.append(int(p1) - 1)
        for i in p2:
            res.append(int(i))
        res.sort(reverse=True)
        # print(total)
        for i, j in enumerate(res, 1):
            total -= j
            if total <= 9:
                print(i)
                break
        # print(res, total)




    pass

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
