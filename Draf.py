from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque

s = "100"


cnt1 = cnt2 = 0

for idx, i in enumerate(s):
    if not (idx % 2 == 0 and i == "0" or (idx % 2 == 1 and i == "1")):
        cnt1 += 1
    elif not (idx % 2 == 0 and i == "1" or (idx % 2 == 1 and i == "0")):
        cnt2 += 1


print(min(cnt1, cnt2))
