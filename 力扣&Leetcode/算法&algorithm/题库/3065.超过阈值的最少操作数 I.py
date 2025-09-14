import bisect


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        return bisect.bisect_left(nums, k)
