from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque
from typing import List


arr = [18, 29, 38, 59, 98, 100, 99, 98, 90]

l, r = 0, len(arr) - 1

while l < r:
    m = (l + r) // 2
    if arr[m - 1] < arr[m] and arr[m] > arr[m + 1]:
        print(m)
        break
    if arr[m - 1] < arr[m] < arr[m + 1]:
        l = m + 1
    elif arr[m - 1] > arr[m] > arr[m + 1]:
        r = m - 1

print(m)
