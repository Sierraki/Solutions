from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate as acc
import heapq
import copy


def p(nums):
    for i in nums:
        print(i)


def lacc(nums):
    return list(acc(nums))


w, h, d = 10, 20, 6
n = 40

each = w * h * d // n

print(each)
