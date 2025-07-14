from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


deck = [1, 2, 3, 4, 4, 3, 2, 1]

cnt = Counter(deck)
print(cnt)
mi = min(cnt.values())

n = 1
while n >= 1:
    if n > mi:
        print(False)
        break
    n += 1
    for j in cnt.values():
        if j % n != 0:
            break
    else:
        print(True)
        break
print(True)
