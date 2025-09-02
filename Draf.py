from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction


nums = [1, 2, 1, 2, 1]
k = 3

prefix = [sum(nums[: i + 1]) for i in range(len(nums))]

print(prefix)
cnt = Counter()
ans = 0

for i in prefix:
    tar = i - k
    if tar in cnt:
        ans += cnt[tar]
    
    cnt[i] += 1

    if i == k:
        ans += 1

print(ans)
