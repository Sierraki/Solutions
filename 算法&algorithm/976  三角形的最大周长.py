from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        mx = 0
        if n < 3:
            return mx
        else:
            cur = sum(nums[:3])
            if nums[0] < nums[1] + nums[2]:
                mx = max(mx, cur)
            for i in range(3, n):
                cur += nums[i] - nums[i - 3]
                if nums[i - 2] < nums[i] + nums[i - 1]:
                    mx = max(mx, cur)
            return mx
