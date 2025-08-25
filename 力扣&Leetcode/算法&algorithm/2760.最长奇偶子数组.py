class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        dp = [0] * (len(nums))
        if nums[0] % 2 == 0 and nums[0] <= threshold:
            dp[0] = 1
        for i in range(1, len(dp)):
            if nums[i] <= threshold:
                if nums[i] % 2 == 0:
                    # 当前为偶数
                    if nums[i - 1] % 2 == 0:
                        # 上一个为偶数
                        dp[i] = 1
                    else:
                        # 上一个为奇数
                        if nums[i - 1] % 2 == 1:
                            dp[i] = 1 + dp[i - 1]
                else:
                    # 当前为奇数
                    if nums[i - 1] % 2 == 0 and dp[i - 1] != 0:
                        # 上一个为偶数
                        dp[i] = dp[i - 1] + 1
                    # 上一个为奇数
                    else:
                        dp[i] = 0
        return max(dp)
