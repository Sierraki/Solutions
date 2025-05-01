class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = defaultdict(int)

        n = len(s)

        cur = 0

        for i in range(n):
            if cnt[s[i]] <2 and max(cnt.values()) <= 2:
                cnt[s[i]] += 1
                cur += 1
            else:
                cnt[s[i]] += 1
                cnt[s[i - cur]] -= 1
                if cnt[s[i - cur]] == 0:
                    del cnt[s[i - cur]]

        return(cur)
