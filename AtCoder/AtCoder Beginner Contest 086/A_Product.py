import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from itertools import accumulate as acc
from math import floor, sqrt

input = sys.stdin.readline
def mii():
    return map(int, input().split())
def lmii():
    return list(map(int, input().split()))
def ii():
    return int(input())
def si():
    return input()[:-1]
def lacc(nums):
    return list(acc(nums))

a, b = mii()
if a*b % 2 == 0:
    print("Even")
else:
    print("Odd")
