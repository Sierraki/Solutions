class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        ans = []
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                ans.append(i - 1)
        if not ans:
            return 0
        elif len(ans) != 1:
            return -1
        else:
            if nums[-1] >= nums[0]:
                return -1
            else:
                return len(nums) - ans[0] - 1
