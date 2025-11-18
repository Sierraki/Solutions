class Solution:
    def permutation(self, S: str) -> List[str]:
        res = []
        n = len(S)
        cnt = [False] * n

        def fun(cur):
            if len(cur) == n:
                res.append(cur.copy())
                return
            for i in range(n):
                if cnt[i] == False:
                    cnt[i] = True
                    cur.append(S[i])
                    fun(cur)
                    cnt[i] = False
                    cur.pop()

        fun([])
        ans = set()
        for i in res:
            cur = "".join(i)
            ans.add(cur)
        return list(ans)
