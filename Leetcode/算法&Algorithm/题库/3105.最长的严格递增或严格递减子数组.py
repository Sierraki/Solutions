class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        mi = 1
        mx = 1
        a = b = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                mx += 1
                a = max(mx, a)
            else:
                mx = 1
            if nums[i - 1] > nums[i]:
                mi += 1
                b = max(mi, b)
            else:
                mi = 1
        return max(a, b)
