class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        pin = len(nums) - 1
        ans = 1
        while nums[pin] >= ans and pin >= 0:
            pin -= 1
            ans += 1
        if pin == len(nums) - 1:
            return -1
        if nums[pin] >= ans - 1 and pin > 0:
            return -1
        return ans - 1
