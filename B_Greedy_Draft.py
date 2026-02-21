from collections import defaultdict, Counter, deque
from math import sqrt, floor,gcd,ceil
from bisect import bisect, bisect_left
from itertools import accumulate as acc
from functools import cache, lru_cache
import heapq
import sys

input = sys.stdin.readline
def mii():
    return map(int, input().split())
def lmii():
    return list(map(int, input().split()))
def ii():
    return int(input())
def si():
    return input().strip()
def lacc(nums):
    return list(acc(nums))
def ms(numss):
    return "".join(map(str, numss))


def solve():
    n,m=mii()
    seen=set()
    for _ in range(n):
        n1=ii()
        nums=lmii()
        nums=[i for i in nums if i not in seen]
        if nums:
            print(nums[0])
            seen.add(nums[0])
            del nums[0]
        else:
            print(0)
        
        
        # print(nums)
        
         
    

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
        solve()
