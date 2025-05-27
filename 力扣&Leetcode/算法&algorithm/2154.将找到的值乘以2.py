class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        print(nums)
        while original >= nums[0] and original <= nums[-1]:
            if original in nums:
                original *= 2
            else:
                break
        return original
