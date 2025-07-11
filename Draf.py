from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque
from typing import List


word = "abcc"

cnt = Counter(word)

mx = max(cnt.values())
mi = min(cnt.values())

a = set([i for i, j in cnt.items() if j == mx])
b = set([i for i, j in cnt.items() if j == mi])

if mx-mi>1 and mi>0:
    print(False)
else:
    if len(b)==1 and mi==1:
        print(True)
    elif len(a)==1 and mx-mi==1:
        print(True)
    elif len(a)==1 and mi==0:
        print(True)
print(False)
