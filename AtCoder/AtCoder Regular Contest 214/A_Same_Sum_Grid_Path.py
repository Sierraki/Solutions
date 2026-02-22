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
    n = ii()
    nums = [lmsi() for _ in range(n)]
    grid = [None for _ in range(2 * n - 1)]
    for i in range(n):
        for j in range(n):
            if nums[i][j] != '?':
                if not grid[i + j]:
                    grid[i + j] = nums[i][j]
                else:
                    if nums[i][j] != grid[i + j]:
                        print(-1)
                        return
    for i in range(n):
        for j in range(n):
            if nums[i][j] == '?':
                if grid[i + j]:
                    nums[i][j] = grid[i + j]
                else:
                    nums[i][j] = '0'
    for i in nums:
        print(''.join(i))

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
