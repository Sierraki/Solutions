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
    n = ii()
    nums = lmii()

    if n == 1:
        print(1)
    elif n == 2:
        if nums[0] <= nums[1]:
            print(n)
        else:
            print(1)
    else:
        for i in range(1, n):
            if nums[i - 1] <= nums[i]:
                continue
            else:
                print(1)
                return
        print(n)



    pass

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
