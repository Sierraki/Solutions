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
    n,d=mii()
    buy=lmii()
    use=lmii()

    res=deque([])
    total=0
    for i in range(n):
        res.append([i+1,buy[i]])
        total+=buy[i]
        cur=use[i]
        total-=cur
        while cur>0:
            if res and res[0][1]>=cur:
                res[0][1]-=cur
                cur=0
            else:
                cur-=res[0][1]
                res[0][1]=0
                res.popleft()
        while res[0][0]<=i+1-d:
            total-=res[0][1]
            res.popleft()
    print(total)
                

        
        
            
    

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
