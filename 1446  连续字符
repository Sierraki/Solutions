class Solution:
    def maxPower(self, s: str) -> int:
        cnt = defaultdict(int)

        left = wl = big = 0

        for idx, i in enumerate(s):
            cnt[i] += 1
            if len(cnt) <= 1:
                wl += 1
                cur = idx - left + 1
                big = max(cur, big)
            else:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
        return(big)
