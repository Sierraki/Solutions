class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"

        def ext(a: str):
            res = []
            for i in a:
                if i != "z":
                    ans = chr(ord(i) + 1)
                elif i == "z":
                    ans = "a"
                res.append(ans)
            a = "".join(list(s) + res)
            return a

        while len(s) < k:
            s = ext(s)
        return s[k - 1]
