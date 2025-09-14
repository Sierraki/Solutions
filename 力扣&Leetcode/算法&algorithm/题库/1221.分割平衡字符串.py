class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = Counter()
        ans = 0
        l = r = 0
        while l <= r and r < len(s):
            cnt[s[r]] += 1
            if cnt["L"] == cnt["R"]:
                ans += 1
                r += 1
                l = r
            else:
                r += 1
        return ans
