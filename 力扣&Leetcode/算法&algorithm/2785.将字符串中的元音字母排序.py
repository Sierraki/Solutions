class Solution:
    def sortVowels(self, s: str) -> str:
        res = []
        ans = []
        for i in s:
            res.append(i)
            if i in "aeiou" or i in "AEIOU":
                ans.append(i)
        ans.sort()
        pin = 0
        for idx, i in enumerate(res):
            if i in "aeiou" or i in "AEIOU":
                res[idx] = ans[pin]
                pin += 1
        return "".join(res)
