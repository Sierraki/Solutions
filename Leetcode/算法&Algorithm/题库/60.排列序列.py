class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        vis = [False] * (n)
        res = []

        def dfs(path):
            if len(res) == k:
                return True
            if len(path) == n:
                cur = "".join(path)
                res.append(cur)
                return
            for i in range(n):
                if not vis[i]:
                    path.append(str(i + 1))
                    vis[i] = True
                    dfs(path)
                    path.pop()
                    vis[i] = False

        dfs([])
        return res[-1]
