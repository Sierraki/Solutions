class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)
        mx = cur = 0
        left = right = 0
        while right < len(nums):
            if nums[right] == nums[left] == target:
                right += 1
                cur += 1
                mx = max(cur, mx)
            else:
                right += 1
                left = right
                cur = 0
        return mx
