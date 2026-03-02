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
    n, x, y = mii()
    nums = lmii()

    p1 = nums[x:y]
    p2 = nums[:x] + nums[y:]
    if not p1:
        print(*p2)
        return
    mi = min(p1)
    mi_idx = p1.index(mi)
    mi2 = p1[mi_idx:] + p1[:mi_idx]
    tar = len(p2)
    for i in range(len(p2)):
        if p2[i] > mi2[0]:
            tar = i
            break
    ans = p2[:tar] + mi2 + p2[tar:]
    print(*ans)
    pass

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
