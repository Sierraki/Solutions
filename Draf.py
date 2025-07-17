from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


nums = [1, 2, 3, 4, 2, 3, 3, 5, 7]

cnt = Counter(nums)

pin = 0

for i in range(0, len(nums), 3):
    print(nums[i : i + 3])
