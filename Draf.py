from collections import defaultdict, Counter
from bisect import bisect
from typing import List
from math import sqrt, floor

nums = [2, 7, 11, 15]
target = 9

a = {}
for idx, i in enumerate(nums):
    goal = target - i
    if goal not in a:
        a[i] = idx
    else:
        print(a[goal], idx)
        break
