class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        nums = [[] for _ in range(n)]
        vis = [False] * n
        for i, j in edges:
            nums[i].append(j)
            nums[j].append(i)

        def dfs(cur):
            if cur == destination:
                return True
            for i in nums[cur]:
                if vis[i] == False:
                    vis[i] = True
                    if dfs(i):
                        return True
            return False

        vis[source] = True
        return dfs(source)
