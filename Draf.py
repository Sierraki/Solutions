from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect
from collections import deque
from typing import List, Optional
from fractions import Fraction
import pandas as pd


str1 = "ABCABC"
str2 = "ABC"

tar=''
m=len(str1)
n=len(str2)

for i in range(min(m,n)):
    