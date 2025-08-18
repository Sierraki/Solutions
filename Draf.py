from collections import defaultdict, Counter
from sortedcontainers import SortedList
from math import sqrt, floor, gcd, lcm, prod, ceil
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction

nums = [[1, 2, 5], [1, 3]]


def fun1(nums):
    if len(nums) > 1:
        for i in range(len(nums)):
            if i < len(nums) - 1:
                nums[i] = str(nums[i]) + "->"
            else:
                nums[i] = str(nums[i])
    else:
        return str(nums[0])
    return "".join(nums)


for i in range(len(nums)):
    print(fun1(i))
