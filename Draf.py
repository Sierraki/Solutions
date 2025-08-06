from collections import defaultdict, Counter
from math import sqrt, floor,gcd
import bisect, re
from collections import deque
from typing import List


nums = [6, 5, 4, 3, 4, 5]

n = len(nums)
lmi = [0] * n
rmi = [0] * n

ans = nums[0]

for i in range(n - 1):
    ans = min(ans, nums[i])
    lmi[i] = min(ans, nums[i])
ans = nums[-1]

for i in range(n - 1, 0, -1):
    ans = min(ans, nums[i])
    rmi[i] = min(ans, nums[i])
print(nums)
print(lmi)
print(rmi)

res = float("inf")
for i in range(2, n - 1):
    if nums[i] > lmi[i - 1] and nums[i] > rmi[i + 1]:
        res = min(res, nums[i] + lmi[i - 1] + rmi[i + 1])
print(res)
