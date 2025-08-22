class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        ans = 0
        tar = nums[0] + nums[1]
        for i in range(1, len(nums), 2):
            if nums[i] + nums[i - 1] == tar:
                ans += 1
            else:
                break
        return ans
