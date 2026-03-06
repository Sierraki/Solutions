class Solution:
    def minFlips(self, s: str) -> int:
        s += s
        nums = [1 if i % 2 == int(j) else 0 for i, j in enumerate(s)]
        cur = 0
        l = 0
        k = len(s) // 2
        ans = float("inf")
        for r, val in enumerate(nums):
            cur += val
            if r >= k - 1:
                ans = min(ans, cur, k - cur)
                cur -= nums[l]
                l += 1
        return ans
