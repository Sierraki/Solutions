import heapq
import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

input = sys.stdin.readline


# num
def ii():
    return int(input())
def mii():
    return map(int, input().split())
def lmii():
    return list(map(int, input().split()))
# string
def lmsi():
    return list(map(str, si()))
def si():
    return input().strip()
def ms(numss):
    return "".join(map(str, numss))
# else
def lacc(nums):
    return list(acc(nums))
def matt(row, col):
    return [[0] * col for _ in range(row)]
def p(numss):
    for i in numss:
        print(i)


def solve():
    n, m = mii()
    nums = [lmii() for _ in range(n)]
    # print(nums)
    # p(nums)
    res = []
    for i in range(m):
        cur = []
        for j in range(n):
            cur.append(nums[j][i])
        res.append(sorted(cur, reverse=True))
    # p(res)

    def fun(ll):
        ans = 0
        n = len(ll)
        for i, j in enumerate(ll):
            ans += (n - i - 1) * j
            ans -= i * j
        return ans
    ans = 0
    for i in res:
        ans += fun(i)
        # print(fun(i), i)
    print(ans)



# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
