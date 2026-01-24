class Solution:
    def permutation(self, S: str) -> List[str]:
        n = len(S)
        res = []
        used = [False] * n

        def bt(cur):
            if len(cur) == n:
                res.append(cur.copy())
                return
            for i in range(n):
                if used[i] == False:
                    used[i] = True
                    cur.append(S[i])
                    bt(cur)
                    used[i] = False
                    cur.pop()

        bt([])
        for i in range(len(res)):
            res[i] = "".join(res[i])
        return res
