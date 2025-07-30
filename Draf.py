from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List

original = [1, 2]
m = 1
n = 1


nums = deque(original)
res = []
while nums:
    for _ in range(m):
        a = [0] * n
        for i in range(n):
            cur = nums.popleft()
            a[i] = cur
        res.append(a)

print(res)
