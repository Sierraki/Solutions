class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        n = len(nums)
        res1 = [1] * n
        res2 = [1] * n
        for i in range(n):
            if i != 0:
                if nums[i - 1] <= nums[i]:
                    res1[i] = res1[i - 1] + 1
        for i in range(n - 1, -1, -1):
            if i != n - 1:
                if nums[i] <= nums[i + 1]:
                    res2[i] = res2[1 + i] + 1
        mx = -float("inf")
        for i in range(n):
            if 0 < i < n - 1:
                if nums[i - 1] <= nums[i + 1]:
                    mx = max(mx, res1[i - 1] + res2[i + 1] + 1)
                else:
                    mx = max(mx, res1[i - 1] + 1, res2[i + 1] + 1)
        mx = max(mx, res1[-2] + 1, res2[1] + 1)
        return mx
