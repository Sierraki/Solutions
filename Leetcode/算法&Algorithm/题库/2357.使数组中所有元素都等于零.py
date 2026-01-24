class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len([i for i in set(nums) if i != 0])
