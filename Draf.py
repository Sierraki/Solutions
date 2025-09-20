from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect, bisect_left
from collections import deque
from typing import List, Optional
from fractions import Fraction


nums = "Codeforces"
tar = "aeiou"

def slove():
    res = ""
    for i in nums:
        if i not in tar:
            res += "." + i.lower()
    print(res)
