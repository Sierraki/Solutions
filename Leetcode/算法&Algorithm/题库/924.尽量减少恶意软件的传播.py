class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        vis = [False] * n
        initial = set(initial)

        def dfs(cur, path):
            path.append(cur)
            vis[cur] = True
            for i, j in enumerate(graph[cur]):
                if j == 1:
                    if not vis[i]:
                        dfs(i, path)

        res = []
        for i in range(n):
            if not vis[i]:
                path = []
                dfs(i, path)
                res.append(path[:])
        ans = []

        def check(tar):
            res = []
            for i in tar:
                if i in initial:
                    res.append(i)
            if len(res) > 1:
                return [[0, i] for i in res]
            elif len(res) == 1:
                return [[len(tar), res[0]]]
            return []

        for i in res:
            cur = check(i)
            if cur:
                ans += cur
        ans.sort(key=lambda x: (-x[0], x[1]))
        return ans[0][1]
