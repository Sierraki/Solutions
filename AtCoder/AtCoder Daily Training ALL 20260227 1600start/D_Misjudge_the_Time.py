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
def msi(): return map(str, input().split())
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
    h, m = mii()

    def check(h, m):
        a = h // 10
        b = h % 10
        c = m // 10
        d = m % 10
        c1 = a * 10 + c
        c2 = b * 10 + d
        return 0 <= c1 <= 23 and 0 <= c2 <= 59

    ans = []

    while 0 <= h <= 24 and 0 <= m <= 59:
        if check(h, m):
            ans = [h, m]
            break
        m += 1
        if m == 60:
            h += 1
            m = 0
            if h == 24:
                h = 0
        # print(h, m)


    print(*ans)

    pass

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
