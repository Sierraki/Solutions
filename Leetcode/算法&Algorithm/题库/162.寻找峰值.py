class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            ans = 0
        else:
            left, right = 0, n - 1
            while left < right:
                mid = (left + right) // 2
                cur = nums[mid]
                cur_left = nums[mid + 1]
                if cur < cur_left:
                    left = mid + 1
                    ans = left
                else:
                    right = mid
                    ans = mid
        return ans
