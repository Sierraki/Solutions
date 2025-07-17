from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
k = 3

l, r = 0, 1

res = []

while l <= r and r < len(nums):
    if nums[r - 1] < nums[r]:
        r += 1
    else:
        res.append([l, r - 1])
        l = r
        r = l + 1
if l < len(nums):
    res.append([l, len(nums) - 1])
print(res)

res = [[i, j] for i, j in res if j - i + 1 >= k]

print(res)


for i in range(len(res)):
    if i >= 2:
        if res[i][0] - 1 == res[i - 1][1]:
            print(True)
            break
    if res[i][1] - res[i][0] + 1 >= 2 * k:
        print(True)
        break
else:
    print(False)
