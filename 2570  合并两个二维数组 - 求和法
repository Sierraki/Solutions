from typing import List
from collections import Counter


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        cnt = Counter()
        nums = nums1 + nums2
        for i in nums:
            if i[0] not in cnt:
                cnt[i[0]] = 0
        for i in nums:
            if i[0] in cnt:
                cnt[i[0]] += i[1]
        a = []
        for i, j in cnt.items():
            a.append([i, j])
        a.sort()
        return a
