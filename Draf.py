from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect, bisect_left
from collections import deque
from typing import List, Optional
from fractions import Fraction

nums = [42, 83, 48, 10, 24, 55, 29, 15, 40]

nums.sort(reverse=True)
n = len(nums) // 2
a = deque(nums[:n])
b = deque(nums[n:])

cnt = 0
while a and b:
    if a[-1] * 2 <= b[-1] or b[-1] * 2 <= a[-1]:
        cnt += 2
        a.pop()
        b.pop()
    else:
        if a[-1] > b[-1]:
            a.pop()
        else:
            b.pop()

print(a)
print(b)
print(cnt)
