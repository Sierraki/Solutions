class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        mx = 1
        for i in nums:
            tar = i + 1
            win = 1
            if i - 1 not in nums:
                while tar in nums:
                    win += 1
                    tar += 1
            mx = max(mx, win)
            if mx * 2 > len(nums):
                break
        return mx
