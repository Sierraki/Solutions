class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        nums = [i for i in range(1, n + 1)]
        nums1 = nums.copy()
        del nums1[-1]
        nums = nums + nums1[::-1]
        del nums[0]
        return nums[time % len(nums) - 1]
