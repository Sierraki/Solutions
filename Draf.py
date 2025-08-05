from collections import defaultdict, Counter
from math import sqrt, floor,gcd
import bisect, re
from collections import deque
from typing import List

nums = [31, 25, 72, 79, 74]

ans = 0

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if gcd(int(str(nums[i])[0]), int(str(nums[j])[-1])) == 1:
            ans+=1

print(ans)
