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
    s = si()

    swap = True
    pin = 0
    
    if n % 2 != 0:
        if s[0] == 'b':
            swap = False
        pin = 1
        
    if swap:
        for i in range(pin, n, 2):
            if (s[i] == 'a' and s[i+1] == 'a') or (s[i] == 'b' and s[i+1] == 'b'):
                swap = False
                break
    if swap:
        print('YES')
    else:
        print('NO')

    pass

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
