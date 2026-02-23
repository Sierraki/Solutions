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
    s = si()
    swap = True
    for i, j in enumerate(s):
        if s[0].lower() == s[0]:
            if i > 0:
                if j.upper() == j:
                    continue
                else:
                    swap = False
                    break
        else:
            if s[0].upper() == s[0]:
                if i > 0:
                    if j.upper() == j:
                        continue
                    else:
                        swap = False
                        break
    if not swap:
        print(s)
    else:
        ans = ''
        for i in s:
            if i.lower() == i:
                ans += i.upper()
            else:
                ans += i.lower()
        print(ans)



# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
