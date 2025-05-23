from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re


nums = [2, 3, -1, 8, 4]
total = sum(nums)
n=len(nums)
for i in range(1, n):
    nums[i] += nums[i - 1]

print(nums, total)

for i in range(n):
    if 