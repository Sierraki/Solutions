from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque
from typing import List


s1 = "this apple is sweet"
s2 = "this apple is sour"

s1 += " " + s2

cnt=Counter(s1.split())

