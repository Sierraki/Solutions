class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0

        cnt = 0

        for right in range( len(nums)):
            if nums[right] == nums[right - 1]:
                cnt += 1
            else:
                cnt = 1

            if cnt <= 2:
                nums[left] = nums[right]
                left += 1

        return len(nums[:left])