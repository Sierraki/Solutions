#时间为On^2
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        cnt = 0

        while cnt < n:
            cnt += 1
            for i in range(1, n):
                if nums[i - 1] > nums[i]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]


        return nums
# 时间为O1
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = i = 0
        right = len(nums) - 1

        # [0,left)为 0 区间
        # [left,i)为 1 区间
        # (right,n-1]为 2 区间

        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1

        return nums
