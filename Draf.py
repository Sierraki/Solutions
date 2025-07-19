from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


nums = [1, 2, 3, 5, 8, 7, 4, 50]
aaa = [1, 3, 6, 11, 19, 26, 30, 80]


def fib(nums: list, x: int) -> int:
    if x == 0:
        return nums[0]
    else:
        return fib(nums, x - 1) + nums[x]


print(fib(nums, 5))
