class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        pin = 1
        while pin < len(nums):
            if nums[pin] == nums[pin - 1]:
                nums[pin] = 0
                nums[pin - 1] *= 2
            pin += 1
        p1 = [i for i in nums if i != 0]
        p2 = [i for i in nums if i == 0]
        return p1 + p2
