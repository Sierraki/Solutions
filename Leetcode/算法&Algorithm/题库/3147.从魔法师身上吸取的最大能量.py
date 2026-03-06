class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = [0] * len(energy)
        ans = -float("inf")
        for i, j in enumerate(energy):
            if i - k >= 0:
                dp[i] = max(j, j + dp[i - k])
            else:
                dp[i] = j
        return max(dp[-k:])
