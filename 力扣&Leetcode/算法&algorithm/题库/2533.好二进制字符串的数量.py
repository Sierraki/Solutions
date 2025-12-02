class Solution:
    def goodBinaryStrings(
        self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int
    ) -> int:
        ans = 0
        dp = [0] * (maxLength + 1)
        for i in range(1, maxLength + 1):
            tar1 = i - oneGroup
            tar2 = i - zeroGroup
            if i == oneGroup:
                dp[i] += 1
            if i == zeroGroup:
                dp[i] += 1
            if tar1 >= 0:
                dp[i] += dp[tar1]
            if tar2 >= 0:
                dp[i] += dp[tar2]
            if i >= minLength:
                ans += dp[i]
                ans %= 10**9 + 7
        return ans
