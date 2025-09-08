from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect
from collections import deque
from typing import List, Optional
from fractions import Fraction
import pandas as pd

s = "abbaca"

res = []
s = deque([i for i in s])

while s:
    cur = s.popleft()
    if not res:
        res.append(cur)
    else:
        if res[-1] == cur:
            res.pop()
        else:
            res.append(cur)
    print(res, s)

print(res)
