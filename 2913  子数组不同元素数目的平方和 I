from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        cur = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                cur += len(set(nums[j - i : j + 1])) ** 2
        return cur
