from typing import List
from collections import Counter


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        cnt = Counter(nums)
        return cnt[target] > n / 2
