class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        nums = [i for i in range(n)]
        nums1 = nums.copy()
        del nums1[-1]
        nums = nums + nums1[::-1]
        del nums[0]
        return nums[k % len(nums) - 1]
