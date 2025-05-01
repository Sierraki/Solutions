class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = defaultdict(int)
        l = 0
        r = 0
        cur = big = 0
        n = len(s)

        while r < n and l <= r:
            if cnt[s[r]] < 1 and len(cnt) == r - l + 1:
                cnt[s[r]] += 1
                cur += 1
                big = max(cur, big)
                r += 1
            else:
                cnt[s[r]] += 1
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    del cnt[s[l]]
                r += 1
                l += 1


        return(big)
