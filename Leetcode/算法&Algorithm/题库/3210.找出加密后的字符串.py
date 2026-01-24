class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        k = k % (n)
        s += s
        res = []
        for i in range(n):
            res.append(s[i + k])
        return "".join(res)
