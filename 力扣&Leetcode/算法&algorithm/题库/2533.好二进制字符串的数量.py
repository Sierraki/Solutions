class Solution:
    def goodBinaryStrings(
        self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int
    ) -> int:
<<<<<<< HEAD
=======
        ans = 0
>>>>>>> df6fadef0c74f684ceec04102a26ef542dbccdaf
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
<<<<<<< HEAD
        res = sum(dp[minLength:]) % (10**9 + 7)
        return res
=======
            if i >= minLength:
                ans += dp[i]
                ans %= 10**9 + 7
        return ans
>>>>>>> df6fadef0c74f684ceec04102a26ef542dbccdaf
