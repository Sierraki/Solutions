import bisect
from collections import Counter, defaultdict
from itertools import count
from datetime import datetime

nums = [1, 3, 6, 10, 12, 15]

cur = cnt = 0
for i in nums:
    if i % 6 == 0:
        cur += i
        cnt += 1
print(cur // cnt)
