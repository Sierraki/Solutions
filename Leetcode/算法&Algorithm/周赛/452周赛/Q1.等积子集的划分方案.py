class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        s = 1
        for i, x in enumerate(nums):
            if (target % x) != 0:
                return False
            s *= x
        if s / target == target:
            return True
        return False
