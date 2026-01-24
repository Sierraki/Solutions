class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        cur = 1
        while cur * k in nums:
            cur += 1
        return cur * k
