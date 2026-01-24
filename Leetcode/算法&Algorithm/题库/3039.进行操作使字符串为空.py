class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        cnt = Counter(s)
        pin = Counter()
        for i in range(len(s)):
            pin[s[i]] = max(pin[s[i]], i)
        mx = max(cnt.values())
        res = {i for i, j in cnt.items() if j == mx}
        pos = [[j, i] for i, j in pin.items()]
        pos.sort(key=lambda x: x[0])
        ans = ""
        for i in pos:
            if i[1] in res:
                ans += i[1]
        return ans
