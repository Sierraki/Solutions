class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        cur = last = nums[0]
        for i in range(1, len(nums)):
            last = cur
            cur += nums[i]
            if cur <= last:
                return last
        return cur
