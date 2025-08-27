from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction


nums = [-2, 0, -1]

s = 1
prefix = []
for i in nums:
    s *= i
    prefix.append(s)
print(prefix)

mi1 = float("inf")  # >0
mi2 = -float("inf")  # <0
mx = -float("inf")
for i in range(1, len(prefix)):
    if prefix[i - 1] > 0:
        mi1 = min(mi1, prefix[i - 1])
    if prefix[i - 1] < 0:
        mi2 = max(mi2, prefix[i - 1])

    mx = max(mx, prefix[i])

    if mi1 != float("inf"):
        mx = max(mx, prefix[i] // mi1)

    if mi2 != -float("inf"):
        mx = max(mx, prefix[i] // mi2)

print(mx)
