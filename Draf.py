from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


nums = [1, 1, 2, 2, 2, 3]

cnt = Counter(nums)

res = [[i, j] for i, j in cnt.items()]
res.sort(key=lambda x: (x[1], -x[0]))

ans = []
for i in range(len(res)):
    ans += [res[i][0]] * res[i][1]

print(ans)
