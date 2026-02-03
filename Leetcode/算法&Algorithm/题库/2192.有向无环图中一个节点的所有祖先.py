class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[j].add(i)
        res = []

        def dfs(cur, path, start, vis):
            if cur != start:
                path.add(cur)
            for i in adj[cur]:
                if i not in vis:
                    vis.add(i)
                    dfs(i, path, start, vis)

        for i in range(n):
            path = set()
            vis = set()
            dfs(i, path, i, vis)
            res.append(sorted(path))
        return res
