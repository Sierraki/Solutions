from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction


a = [1, 1]
b = [2, 3]
c = [1, 5]


def fun1(num=int) -> bool:
    return bin(num)[2:].count("1") % 2 == 0


def fun2(nums=list) -> int:
    ans = nums[0]
    for i in range(1, len(nums)):
        ans ^= nums[i]
    return ans


ans = 0
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            res = fun2([a[i], b[j], c[k]])
            if fun1(res):
                ans += 1
print(ans)
