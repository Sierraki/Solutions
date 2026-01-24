class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res = sentence.split()

        def fun(ans=str):
            if ans[0].lower() in "aeiou":
                return ans + "ma"
            else:
                p1 = ans[0]
                p2 = ans[1:]
                return p2 + p1 + "ma"

        ans = []
        for i in range(len(res)):
            ans.append(fun(res[i]) + "a" * (i + 1))
        res1 = " ".join(ans)
        return res1
