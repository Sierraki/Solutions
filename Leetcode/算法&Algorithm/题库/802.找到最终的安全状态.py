class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        vis = [0] * n

        # 0 没有遍历 1 遍历过 2 安全
        def dfs(cur):
            if vis[cur] > 0:
                return vis[cur] == 2
            vis[cur] = 1
            for i in graph[cur]:
                if not dfs(i):
                    return False
            vis[cur] = 2
            return True

        for i in range(n):
            dfs(i)
        return [i for i, j in enumerate(vis) if j == 2]
