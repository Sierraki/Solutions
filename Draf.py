from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque
from typing import List


nums = [-4, -2, 1, 4, 8]

ans = -float("inf")
d = float("inf")

for i in nums:
    if abs(i) < d:
        ans = i
        d = abs(i)
    elif abs(i) == d:
        if i > ans:
            ans = i
print(ans)
