from collections import defaultdict, Counter
from sortedcontainers import SortedList
from math import sqrt, floor, gcd, lcm, prod, ceil
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction

time = "07:?3"

a = time[0]
b = time[1]
c = time[3]
d = time[4]

ans1 = ans2 = 1

# hours
if a == "?":
    if b == "?":
        # ??
        ans1 = 24
    else:
        # ?x
        if int(b) <= 3:
            ans1 = 3
        else:
            ans1 = 2
else:
    # x?
    if int(a) <= 1:
        ans1 = 10
    else:
        ans1 = 2


if c == "?":
    if d == "?":
        ans2 = 60
    else:
        ans2 = 10
else:
    if d == "?":
        ans2 = 10


print(ans1, ans2, ans1 * ans2)
