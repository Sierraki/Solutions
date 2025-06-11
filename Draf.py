from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

n = 521

res = 0
for idx, i in enumerate(str(n)):
    if idx % 2 == 0:
        res += int(i)
    else:
        res -= int(i)
print(res)
