from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache


nums1 = [3, 5, 2, 6]
nums2 = [3, 1, 7]

nums1.sort()
nums2.sort()
ans1 = str(nums1[0]) + str(nums2[0])
ans2 = str(nums2[0]) + str(nums1[0])
mi = min(int(ans1), int(ans2))
p1, p2 = 0, 0

while p1 < len(nums1) and p2 < len(nums2):
    if nums1[p1] == nums2[p2]:
        mi = min(mi, nums1[p1])
        break
    if nums1[p1] > nums2[p2]:
        p2 += 1
    else:
        p1 += 1

print(mi)
