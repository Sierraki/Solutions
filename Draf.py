from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re


s = "abccbaacz"

cnt=Counter()

for i in s:
    cnt[i] += 1
    if cnt[i]==2:
        
