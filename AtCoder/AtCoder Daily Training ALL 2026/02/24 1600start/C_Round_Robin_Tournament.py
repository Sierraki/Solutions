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
    nums = [lmsi() for _ in range(n)]
    cnt = Counter([i for i in range(1, n + 1)])
    for i in range(n):
        for j in range(n):
            cur = nums[i][j]
            if cur == 'o':
                cnt[i + 1] += 1
                cnt[j + 1] -= 1
    res = [[i, j] for i, j in cnt.items()]
    res.sort(key=lambda x: (-x[1], x[0]))
    print(*[i[0] for i in res])
    pass

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
