class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = sorted(set(nums), reverse=True)
        if len(set(nums)) < 3:
            return max(nums)
        else:
            return a[2]
