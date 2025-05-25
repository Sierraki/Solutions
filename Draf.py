from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

matrix = [[-5]]
target = -2

a = [j for i in matrix for j in i]
if not a:
    print(False)
a.sort()
print(a)
lc = bisect.bisect_left(a, target)
lc1 = bisect.bisect(a, target)

print(a[lc1-1] == target or a[lc-1] == target)
