from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque

nums = [4, 3, 1, 6]

for i in range(1,len(nums)):
    if abs(nums[i-1]-nums[i])%2==0:
        return False
return True    