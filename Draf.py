from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect, bisect_left
from collections import deque
from typing import List, Optional
from fractions import Fraction


s = "bbaa"
c = "b"

tar = [idx for idx in range(len(s)) if s[idx] == c]
nums = list(range(len(s)))

if len(tar) > 1:
    pin = 0
    for i in range(len(nums)):
        while nums[i] >= tar[pin] and pin < len(tar) - 1:
            pin += 1

        if pin == len(tar) - 1 or nums[i] < tar[pin] or i == len(nums) - 1:
            if pin >= 1:
                nums[i] = min(abs(i - tar[pin]), abs(i - tar[pin - 1]))
            else:
                nums[i] = abs(i - tar[pin])
        elif nums[i] == tar[pin]:
            nums[i] = 0


else:
    for i in range(len(nums)):
        nums[i] = abs(nums[i] - tar[0])

print(tar)
print(nums)
print([3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])
