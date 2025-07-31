from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


nums = [1, 5, 0, 3, 5]


res = list(set([i for i in nums if i != 0]))

res.sort()
tar = res[-1]
del res[-1]
if not res:
    print(0)
if sum(res) != tar:
    ans = len(res) + 1
else:
    ans = len(res)

print(ans)
