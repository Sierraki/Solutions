class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        j=len(nums)

        if target > nums[j-1]:
            return j 
        for i in nums:
            if i >= target:
                a=nums.index(i)
                return a
                