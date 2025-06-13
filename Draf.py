from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache


details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]

res = 0

for i in details:
    if int(i[11:13])>60:
        res+=1
return res
