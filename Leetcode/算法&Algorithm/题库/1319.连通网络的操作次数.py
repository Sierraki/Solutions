class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        cable = len(connections)
        nums = [[] for _ in range(n)]
        for i, j in connections:
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
                res.append((path[:]))
        cur = 0
        for i in res:
            cur += len(i) - 1
        if len(res) == 1:
            ans = 0
        if len(res) - 1 + cur > cable:
            ans = -1
        else:
            ans = len(res) - 1
        return ans
