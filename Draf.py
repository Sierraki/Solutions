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


def fun(nums):
    for i in range(1, len(nums)):
        if 1 <= abs(nums[i] - nums[i - 1]) <= 2:
            continue
        else:
            return False

    return 1 <= abs(nums[0] - nums[-1]) <= 2


n = 5


def fun1(n):
    nums = list(range(1, n + 1))

    res = []

    while n >= 2:
        cur1 = n - 1
        cur2 = n - 2
        n -= 2
        if not res:
            res += [cur1, cur2] * cur2 + [cur1]
        else:
            res = [cur1] + res + [cur1, cur2] * cur2
    if n==1:
        res.append(1)
    return res


for i in range(3, 1000 + 1):
    cur = fun1(i)

    if fun(cur):
        print(i, fun(cur))
    else:
        print(i)
        break

print(fun1(4))
