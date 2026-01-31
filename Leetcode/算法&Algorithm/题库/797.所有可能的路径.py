class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ma = [[0] * n for _ in range(n)]
        res = []
        path = []

        def dfs(cur, path):
            if cur == n - 1:
                res.append(path.copy())
                return

            for i in graph[cur]:

                path.append(i)
                dfs(i, path)
                path.pop()

        dfs(0, [0])
        return res
