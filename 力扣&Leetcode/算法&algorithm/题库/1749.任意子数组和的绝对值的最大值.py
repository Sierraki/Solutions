class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s = 0
        prefix = []
        for i in nums:
            s += i
            prefix.append(s)
        mi = mx = prefix[0]
        ans = abs(prefix[0])
        for i in range(1, len(prefix)):
            mi = min(mi, prefix[i - 1])
            mx = max(mx, prefix[i - 1])
            ans = max(abs(prefix[i]), abs(prefix[i] - mi), abs(prefix[i] - mx), ans)
        return ans
