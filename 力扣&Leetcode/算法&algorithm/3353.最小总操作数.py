class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ac = 0
        cnt = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + ac != nums[i + 1]:
                cnt += 1
                nums[i] += ac
                ac += nums[i + 1] - nums[i]
            nums[i] = nums[i + 1]
        return cnt
