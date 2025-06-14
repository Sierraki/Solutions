from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache


n = 783
nums = str(n) + str(2 * n) + str(3 * n)
cnt=Counter()

for i in nums:
    cnt[i]+=1
    if cnt[i]>1 or i=='0':
        print(False)
if len(cnt)!=9:
    return False
return True
    
