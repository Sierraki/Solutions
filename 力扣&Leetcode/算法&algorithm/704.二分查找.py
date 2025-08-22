class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            if nums[mid] == target:
                break
        ans = -1
        if nums[mid] == target:
            ans = mid
        return ans
