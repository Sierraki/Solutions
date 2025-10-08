class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        cnt = dict(zip(order, [str(i).zfill(2) for i in range(1, 27)]))
        mx = 0
        for i in words:
            mx = max(mx, len(i))

        def fun(res=str) -> int:
            ans = ""
            for i in res:
                ans += cnt[i]
            if len((ans)) < mx * 2:
                ans += "0" * (mx * 2 - len(ans))
            return int(ans)

        for i in range(1, len(words)):
            if fun(words[i - 1]) > fun(words[i]):
                return False
        return True
