class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for idx, i in enumerate(nums):
            if idx >= 1:
                if nums[idx - 1] >= i:
                    cnt += nums[idx - 1] - i + 1
                    nums[idx] = nums[idx - 1] + 1
        return cnt
