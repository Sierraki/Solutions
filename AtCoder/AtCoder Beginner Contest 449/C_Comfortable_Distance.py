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



def solve():
    n, l, r = mii()
    s = si()
    cnt = defaultdict(list)
    for i, j in enumerate(s, 1):
        cnt[j].append(i)
    # print(cnt)

    def fun(nums, l, r):
        count = 0
        for b_idx in range(len(nums)):
            current_val = nums[b_idx]
            lower_bound = current_val - r
            upper_bound = current_val - l
            i_left = bisect_left(nums, lower_bound)
            i_right = bisect(nums, upper_bound)
            if i_right > i_left:
                count += (i_right - i_left)
        return count

    ans = 0
    for i in cnt.values():
        ans += fun(i, l, r)
    print(ans)
    pass



# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
