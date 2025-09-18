from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect
from collections import deque
from typing import List, Optional
from fractions import Fraction
import pandas as pd


nums = [3, 8, 1, 3, 2, 1, 8, 9, 0]
firstLen = 3
secondLen = 2

s = 0
prefix = []
for i in nums:
    s += i
    prefix.append(s)


print(prefix)
top = [prefix[firstLen - 1]] + [
    prefix[i] - prefix[i - firstLen] for i in range(firstLen, len(prefix))
]
down = [prefix[secondLen - 1]] + [
    prefix[i] - prefix[i - secondLen] for i in range(secondLen, len(prefix))
]

print(top)
print(down)
dp = [[0] * (len(nums)) for _ in range(len(nums))]





print(dp)
