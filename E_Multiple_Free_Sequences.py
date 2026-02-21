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
    m,a,b=mii()

    adj = [[] for _ in range(m * m)]
    for i in range(m):
        for j in range(m):
            w = (a * j + b * i) % m
            nextt = j * m + w
            cur = i * m + j
            adj[nextt].append(cur)
            
    res = deque()
    vis = [False] * m*m
    
    for i in range(m):
        s1 = i  
        if not vis[s1]:
            vis[s1] = True
            res.append(s1)
            
        s2 = i * m 
        if not vis[s2]:
            vis[s2] = True
            res.append(s2)
            
    cnt = 0
    while res:
        cur = res.popleft()
        cnt += 1
        for prev in adj[cur]:
            if not vis[prev]:
                vis[prev] = True
                res.append(prev)
                
    print(m * m - cnt)
    pass

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
        solve()
