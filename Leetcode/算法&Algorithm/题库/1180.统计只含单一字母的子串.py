class Solution:
    def countLetters(self, s: str) -> int:
        pin = 0
        ans = 0
        res = []
        for i in range(len(s)):
            if s[i] != s[pin]:
                res.append(s[pin:i])
                ans += i - 1 - pin
                last = s[pin:i]
                pin = i
        if res:
            if s[pin:] != res[-1]:
                res.append(s[pin:])
        else:
            res.append(s[pin:])
        for i in res:
            ans += (1 + len(i)) * len(i) // 2
        return ans
