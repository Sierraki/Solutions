from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque


a = "*"

for i in range(2, -1, -1):
    print(" " * (i) + a * (5 - i * 2) + " " * (i))
