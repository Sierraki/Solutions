from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List

nums = [1, 4, 5, 2, 3]
k = 3

ans = -float("inf")

for i in range(k - 1, len(nums)):
    ans = max(ans, int("".join(map(str, nums[i - k + 1 : i + 1]))))

res = [i for i in str(ans)]
print(res)
