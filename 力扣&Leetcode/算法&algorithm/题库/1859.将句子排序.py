class Solution:
    def sortSentence(self, s: str) -> str:
        res = s.split()
        cnt = {int(i[-1]): i[:-1] for i in res}
        ans = [0] * len(cnt)
        for i in range(len(ans)):
            ans[i] = cnt[i + 1]
        a = []
        for i in ans:
            a += i + " "
        del a[-1]
        return "".join(a)
