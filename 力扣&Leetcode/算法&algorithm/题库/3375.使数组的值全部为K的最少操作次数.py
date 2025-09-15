class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        if min(nums) < k:
            return -1
        return sum([1 for i in nums if i > k])
