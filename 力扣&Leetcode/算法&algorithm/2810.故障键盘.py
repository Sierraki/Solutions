class Solution:
    def finalString(self, s: str) -> str:
        pin = 0
        while s[0] == "i":
            s = s[1:]

        while pin < len(s):
            if s[pin] == "i":
                p1 = s[:pin]
                p2 = s[pin + 1 :]
                s = p1[::-1] + p2
                pin -= 1
            else:
                pin += 1
        return s
