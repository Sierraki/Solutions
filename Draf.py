from collections import defaultdict, Counter
from bisect import bisect
from typing import List
from math import sqrt, floor

strs = ["alic3", "bob", "3", "4", "00000"]


mx = 0
for idx, i in enumerate(strs):
    if i.isdigit():
        strs[idx] = int(i)
    else:
        strs[idx] = len(i)
    mx = max(strs[idx], mx)
print(mx)
