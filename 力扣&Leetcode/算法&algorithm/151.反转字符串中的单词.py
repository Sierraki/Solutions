class Solution:
    def reverseWords(self, s: str) -> str:
        res = [i for i in s.split()]
        res = res[::-1]
        for i in range(len(res) - 1, 0, -1):
            res.insert(i, " ")
        return "".join(res)
