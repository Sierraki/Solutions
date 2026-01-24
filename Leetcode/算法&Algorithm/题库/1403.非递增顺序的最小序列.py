class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        c = sum(nums)
        s = 0
        nums.sort(reverse=True)
        for idx, i in enumerate(nums):
            s += i
            c -= i
            if s > c:
                return nums[: idx + 1]
