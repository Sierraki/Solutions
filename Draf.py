from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect
from collections import deque
from typing import List, Optional
from fractions import Fraction
import pandas as pd
<<<<<<< HEAD

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
=======
import math


n = 1


res1 = [i for i in range(1, n // 2 + 1)]
res2 = [-i for i in range(1, n // 2 + 1)]
if n % 2 == 1:
    ans = res1 + res2 + [0]
else:
    ans = res1 + res2

print(ans)
>>>>>>> 93addac0863600c68a2f06a971795f5c06d99147
