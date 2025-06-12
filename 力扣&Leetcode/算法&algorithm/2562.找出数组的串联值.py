class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0
        if len(nums) % 2 == 1:
            mid = len(nums) // 2
            res += nums[mid]
            del nums[mid]
        left, right = 0, len(nums) - 1
        while left < right:
            ans = int(str(nums[left]) + str(nums[right]))
            res += ans
            left += 1
            right -= 1
        return res
