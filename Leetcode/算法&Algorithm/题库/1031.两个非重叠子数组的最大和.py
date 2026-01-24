class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        s = 0
        prefix = []
        for i in nums:
            s += i
            prefix.append(s)
        top = (
            [0] * (firstLen - 1)
            + [prefix[firstLen - 1]]
            + [prefix[i] - prefix[i - firstLen] for i in range(firstLen, len(prefix))]
        )
        down = (
            [0] * (secondLen - 1)
            + [prefix[secondLen - 1]]
            + [prefix[i] - prefix[i - secondLen] for i in range(secondLen, len(prefix))]
        )
        dp = [[0] * (len(nums)) for _ in range(len(nums))]
        ans = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if (0 <= i - secondLen + 1 <= i <= j - firstLen <= j) or (
                    0 <= j - firstLen + 1 <= j <= i - secondLen <= i
                ):
                    dp[i][j] = top[j] + down[i]
                    ans = max(ans, dp[i][j])
        return ans
