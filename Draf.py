from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect
from collections import deque
from typing import List, Optional
from fractions import Fraction
import pandas as pd

s = "aaba"
c = "b"

tar = []
for idx, i in enumerate(s):
    if i == c:
        tar.append(idx)
pin = 1
if len(tar) == 1:
    pin = 0
res = list(range(len(s)))

print(res)

for i in range(len(res)):
    if res[i] > tar[pin] and len(tar) > 1:
        pin += 1
    if res[i] == tar[pin]:
        res[i] = 0
    else:
        if len(tar) > 1:
            res[i] = min(abs(res[i] - tar[pin]), abs(res[i] - tar[pin - 1]))
        else:
            res[i] = abs(res[i] - tar[pin])
    print(pin)

print(res)
print(tar)
