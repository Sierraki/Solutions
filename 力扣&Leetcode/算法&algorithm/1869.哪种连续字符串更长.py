class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        def fun(s: str, tar: str):
            mx = 0
            ans = 0
            for i in s:
                if i == tar:
                    ans += 1
                else:
                    ans = 0
                mx = max(mx, ans)
            return mx

        return fun(s, "1") > fun(s, "0")
