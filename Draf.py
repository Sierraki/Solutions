from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect
from collections import deque
from typing import List, Optional
from fractions import Fraction
import pandas as pd
import math


n = 1


res1 = [i for i in range(1, n // 2 + 1)]
res2 = [-i for i in range(1, n // 2 + 1)]
if n % 2 == 1:
    ans = res1 + res2 + [0]
else:
    ans = res1 + res2

print(ans)
