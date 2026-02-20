class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(i, n):
                cnt[s[j]] += 1
                if len(set(cnt.values())) == 1:
                    ans = max(ans, j - i + 1)
        return ans
