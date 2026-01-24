class Solution:
    def freqAlphabets(self, s: str) -> str:
        pin = len(s) - 1
        cnt = {i - 96: chr(i) for i in range(ord("a"), ord("z") + 1)}
        res = ""
        while pin >= 0:
            if s[pin].isdigit():
                res += cnt[int(s[pin])]
                pin -= 1
            elif s[pin] == "#":
                res += cnt[int(s[pin - 2 : pin])]
                pin -= 3
        return res[::-1]
