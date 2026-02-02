class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        nums = [[] for _ in range(n)]
        for i, j in edges:
            nums[i].append(j)
            nums[j].append(i)
        vis = [False] * n
        res = []

        def dfs(cur, path):
            vis[cur] = True
            path.append(cur)
            for i in nums[cur]:
                if not vis[i]:
                    dfs(i, path)

        for i in range(n):
            if not vis[i]:
                path = []
                dfs(i, path)
                res.append(len(path))
        ans = 0
        total = sum(res)
        for i in res:
            total -= i
            ans += i * total
        return ans
