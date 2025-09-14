class Solution:
    def modifyString(self, s: str) -> str:
        if len(s) == 1 and s[0] == "?":
            return "a"
        s = [i for i in s]

        def fun(a: str, b: str) -> str:
            res = 97
            if not a:
                while chr(res) == b:
                    res += 1
            elif not b:
                while chr(res) == a:
                    res += 1
            else:
                while chr(res) == b or chr(res) == a:
                    res += 1
            return chr(res)

        pin = 0
        for pin in range(len(s)):
            if s[pin] == "?":
                if pin == 0:
                    s[pin] = fun(None, s[pin + 1])
                elif pin == len(s) - 1:
                    s[pin] = fun(s[pin - 1], None)
                else:
                    s[pin] = fun(s[pin - 1], s[pin + 1])
            pin += 1
        return "".join(s)
