from collections import Counter
from typing import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        cnt = Counter(nums)
        return cnt[target] > n / 2
