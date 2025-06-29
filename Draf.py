from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque

price = [8, 21, 27, 34, 52, 66]
target = 61


for i in price:
    tar = target - i
    lc = bisect.bisect_left(price, tar)
    if tar == price[lc]:
        print(tar, i)
