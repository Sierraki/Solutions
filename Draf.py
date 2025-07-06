from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque
from typing import List


nums = [1, 2, 3, 4]

res = 0
for i in nums:
    ans1 = i // 3
    ans2 = ans1 + 1
    res += min(abs(ans2 * 3 - i), abs(ans1 * 3 - i))
print(res)
