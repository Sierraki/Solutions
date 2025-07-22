from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List

dimensions = [[2, 6], [5, 1], [3, 10], [8, 4]]

mx = -float("inf")
ans = -float("inf")


for i in dimensions:
    if sqrt(i[0] ** 2 + i[1] ** 2) > mx:
        ans = i[0] * i[1]
    elif sqrt(i[0] ** 2 + i[1] ** 2) == mx:
        ans = max(ans, i[0] * i[1])
print(ans)
