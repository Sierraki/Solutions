class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        if (nums[0] - nums[1]) == -1:
            dp[1] = 2
        for i in range(2, len(dp)):
            if abs(nums[i] - nums[i - 1]) == 1:
                # 判断前一个是增还是减
                increase = True
                if nums[i - 2] + 1 == nums[i - 1]:
                    increase = True
                    dp[i] = 2
                elif nums[i - 2] - 1 == nums[i - 1]:
                    increase = False
                    dp[i] = 2
                # 判断当前状态
                if nums[i - 1] < nums[i]:
                    if increase == False:
                        if dp[i - 1] != 0:
                            dp[i] = dp[i - 1] + 1
                    else:
                        dp[i] = 2

                if nums[i - 1] > nums[i]:

                    if nums[i - 2] + 1 == nums[i - 1]:
                        if dp[i - 1] != 0:
                            dp[i] = dp[i - 1] + 1
                    else:
                        dp[i] = 0
        ans = max(dp)
        if ans == 0:
            return -1
        return ans
