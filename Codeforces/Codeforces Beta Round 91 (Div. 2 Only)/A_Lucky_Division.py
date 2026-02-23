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



def solve():
    n = ii()

    def fun(k):
        res = deque([''])
        while len(res[0]) < k:
            cur = res.popleft()
            res.append(cur + '4')
            res.append(cur + '7')
        return res
    tar = []
    for i in range(1, len(str(n)) + 1):
        tar += fun(i)
    for i in tar:
        if n % int(i) == 0:
            print('YES')
            break
    else:
        print('NO')

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
