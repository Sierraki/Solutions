from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction

res = [[4, 9, 5], [4, 9, 1], [4, 0]]

ans = 0
for i in res:
    a = ""
    for j in i:
        a += str(j)
    ans += int(a)

print(ans)
