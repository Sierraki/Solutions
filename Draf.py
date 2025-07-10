from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque
from typing import List

nums = [1, 3, 5, 2, 4, 8, 2, 2]


def fun(nums: list) -> list:
    res = []
    for i in range(0, len(nums), 2):
        if i % 4 == 0:
            ans = min(nums[i], nums[i + 1])
        else:
            ans = max(nums[i], nums[i + 1])
        res.append(ans)
    return res


if len(nums) == 1:
    print(nums[0])
else:
    while len(nums) >= 2:
        nums = fun(nums)
    print(nums[0])
