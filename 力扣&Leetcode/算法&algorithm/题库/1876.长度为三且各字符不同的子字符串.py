class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        c = 0
        if n >= 3:
            cnt = Counter(s[:3])
            if len(cnt) == 3:
                c += 1
            for i in range(3, n):
                cnt[s[i]] += 1
                cnt[s[i - 3]] -= 1
                if cnt[s[i - 3]] == 0:
                    del cnt[s[i - 3]]
                if len(cnt) == 3:
                    c += 1
                print(cnt, c)
        return c
