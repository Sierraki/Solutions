class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        n = len(s)
        res = []
        pin = 0
        for i in range(1, n):
            if s[i] == s[pin]:
                if i == n - 1:
                    if s[i - 1] == s[pin] and i - pin >= 2:
                        res.append([pin, i])
                else:
                    if s[pin] != s[pin + 1]:
                        pin = i - 1
                    continue
            elif s[i] != s[pin] or i == n - 1:
                if s[i - 1] == s[pin]:
                    if i - 1 - pin >= 2:
                        res.append([pin, i - 1])
                        pin = i
                pin = i - 1
        return res
