class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return min(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid] <= nums[right]:
                ans = left
                break
            elif nums[left] <= nums[mid]:
                ans = mid
                left = mid + 1
            else:
                right = mid
        return nums[ans]
