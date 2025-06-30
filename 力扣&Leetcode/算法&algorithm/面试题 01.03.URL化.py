class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        res = []
        for i in range(length):
            if S[i] == " ":
                res.append("%20")
            else:
                res.append(S[i])
        return "".join(res)
