class Solution:
    def oddString(self, words: List[str]) -> str:
        cnt = defaultdict(list)

        def fun(x: str) -> str:
            res = ""
            for i in range(1, len(x)):
                res += str(ord(x[i]) - ord(x[i - 1])) + "0"
            return res

        for i in words:
            cnt[fun(i)].append(i)
        ans = [i for i in cnt.values() if len(i) == 1]
        return ans[0][0]
