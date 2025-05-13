from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums += nums
        mx = -1
        for i in range(1, len(nums)):
            mx = max(abs(nums[i] - nums[i - 1]), mx)
        return mx
