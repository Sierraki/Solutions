from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List

word = "acolkxjbizfmhnrdq"

n = len(word)

a = n // 8
b = n % 8

res = 0
if a == 0:
    res = b
elif a == 1:
    res = 8 + b * 2
else:
    res = (1 + a) * a * 4 + b * (a + 1)

print(res)
