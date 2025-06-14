from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache


nums = [3, 2, 1, 4]
res = sorted(list(set(nums)))
print(res)
ans=-1
if len(res)>2:
    ans=res[2]