class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = []
        s = 0
        mi = float("inf")
        for i in nums:
            s += i
            prefix.append(s)
        mx = prefix[0]
        for i in range(1, len(prefix)):
            mi = min(mi, prefix[i - 1])
            mx = max(prefix[i], prefix[i] - mi, mx)
        return mx
