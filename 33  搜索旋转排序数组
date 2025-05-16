class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        if target == nums[left]:
            return left
        elif target > nums[left] and target <= nums[-1]:
            a = nums[left : len(nums)]
            lc = bisect.bisect_left(a, target)
            if a[lc] == target:
                return left + lc
            else:
                return -1
        else:
            a = nums[: left - 1]
            lc = bisect.bisect_left(a, target)
            if nums[lc] == target:
                return lc
            else:
                return -1
