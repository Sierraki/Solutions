from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque

numbers = [1, 2, 4, 6, 10]
target = 8

ans = -1
check = Counter()
for idx, i in enumerate(numbers):
    tar = target - i
    if tar not in check:
        check[tar] += idx
    if i in check:
        ans = [check[i], idx]
print(ans)
