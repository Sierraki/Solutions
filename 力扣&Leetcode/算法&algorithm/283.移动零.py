class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for i in range(1, len(nums)):
            while nums[l] != 0 and l < len(nums) and l < i:
                l += 1
            if nums[i] != 0:
                nums[l], nums[i] = nums[i], nums[l]
        return nums
