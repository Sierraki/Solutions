from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

s1 = "bank"
s2 = "kanb"

s1 = [i for i in s1]
s2 = [i for i in s2]

mapp = {i: idx for idx, i in enumerate(s1)}
# 环检测
print(mapp)
for i in range(len(s1)):
    
