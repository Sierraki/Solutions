from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


n = 4

res = set()

for i in range(1, floor(sqrt(n)) + 1):
    if n % i == 0:
        res.add(i)
        res.add(n // i)

print(res)
