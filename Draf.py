from collections import defaultdict, Counter
from sortedcontainers import SortedList
from math import sqrt, floor, gcd, lcm, prod, ceil
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction

n = 5


def fun(n=int):
    for i in range(floor(sqrt(n)) + 1):
        if 2**i == n:
            return i
    return False


if fun(n):
    return fun(n)
return n