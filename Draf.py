from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
import logging

a = 18
b = 6

tar = min(a, b)

last = 1
for i in range(2, tar + 1):
    if a % i == 0 and b % i == 0:
        last = i
return last
