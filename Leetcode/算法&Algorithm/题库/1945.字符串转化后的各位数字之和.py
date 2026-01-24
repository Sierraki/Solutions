class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def fun(n: str) -> str:
            s = 0
            for i in n:
                s += int(i)
            return str(s)

        cnt = Counter()
        for i in range(ord("a"), ord("z") + 1):
            cnt[chr(i)] = str(i - 96)
        ans = ""
        for i in s:
            ans += cnt[i]
        for _ in range(k):
            ans = fun(ans)
        return int(ans)
