class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res = s.split()
        ans = []
        for i in range(k):
            ans += res[i] + " "
        del ans[-1]
        return "".join(ans)
