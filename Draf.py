from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


nums = [-1, 2, -3, 3]

po = [i for i in nums if i > 0]
ne = {i for i in nums if i < 0}


ans = -1
for i in po:
    if -i in ne:
        ans = max(i, ans)

print(ans)
