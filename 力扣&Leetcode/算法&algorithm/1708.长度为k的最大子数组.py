class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        ans = -float("inf")
        idx = -float("inf")
        for i in range(len(nums) - k + 1):
            if nums[i] > ans:
                ans = nums[i]
                idx = i
        return nums[idx : idx + k]
