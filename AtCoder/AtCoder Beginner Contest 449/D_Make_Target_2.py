import heapq
import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt, pi

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



def fun1(X, Y):
    if X < 0 or Y < 0:
        return 0
    if X > Y:
        X, Y = Y, X
    m = X // 2
    ans = (2 * m + 1) * (m + 1)
    def fun2(n):
        if n < 0:
            return 0
        return n // 2 + 1
    even_cnt = fun2(Y) - fun2(X)
    ans += (X + 1) * even_cnt
    return ans

def countt(low, high):
    if low > 0: 
        return [(1, high), (-1, low - 1)]
    if high < 0: 
        return [(1, abs(low)), (-1, abs(high) - 1)]
    return [(1, high), (1, abs(low)), (-1, 0)]

def solve():

    l, r, d, u = mii()

    row = countt(l, r)
    col = countt(d, u)

    black_cnt = 0
    for i, j in row:
        for ii, jj in col:
            black_cnt += i * ii * fun1(j, jj)

    print(black_cnt)



# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
