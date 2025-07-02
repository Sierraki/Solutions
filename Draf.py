from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque

m = 18
n = 3
ops = [
    [16, 1],
    [14, 3],
    [14, 2],
    [4, 1],
    [10, 1],
    [11, 1],
    [8, 3],
    [16, 2],
    [13, 1],
    [8, 3],
    [2, 2],
    [9, 1],
    [3, 1],
    [2, 2],
    [6, 3],
]

res1 = [i for i, j in ops]
res2 = [j for i, j in ops]

print(min(res1) * min(res2))
