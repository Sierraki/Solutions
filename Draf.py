from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


nums = [1, 1, 1, 2, 2, 3]
k = 2

cnt = Counter(nums)
res = [[i, j] for i, j in cnt.items()]
res.sort(key=lambda x: x[1], reverse=True)
ans = []
for i in range(k):
    if i < len(res):
        ans.append(res[i][0])
print(ans)
