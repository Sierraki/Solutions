class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(2, n):
            if nums[i] + nums[i - 2] == 0.5 * nums[i - 1]:
                cnt += 1
        return cnt
