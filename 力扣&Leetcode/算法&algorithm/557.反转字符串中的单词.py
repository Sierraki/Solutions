class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for i in s.split():
            res.append(i[::-1])
            res.append(" ")
        return "".join(res[:-1])
