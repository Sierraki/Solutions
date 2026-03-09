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
    s1 = si()
    s2 = si()
    res1 = [i for i in s1 if i != 'A']
    res2 = [i for i in s2 if i != 'A']
    if res1 != res2:
        print(-1)
        return

    def fun(s):
        res = []
        cur = 0
        for i in s:
            if i == 'A':
                cur += 1
            else:
                res.append(cur)
                cur = 0
        res.append(cur)
        return res
    tar1 = fun(s1)
    tar2 = fun(s2)
    ans = 0
    for i in range(len(tar1)):
        ans += abs(tar1[i] - tar2[i])
    print(ans)
    pass


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
