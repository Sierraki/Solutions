class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:  # 如果当前元素不为 0
                nums[left], nums[right] = nums[right], nums[left]  # 交换位置
                left += 1  # 移动左指针

        return nums
