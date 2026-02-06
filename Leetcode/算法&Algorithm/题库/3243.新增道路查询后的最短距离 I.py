# DP
class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        dp = [i for i in range(n)]
        adj = defaultdict(list)
        for i in range(n - 1):
            adj[i].append(i + 1)
        res = []
        for u, v in queries:
            adj[u].append(v)
            if dp[u] + 1 < dp[v]:
                dp[v] = dp[u] + 1
                nums = deque([v])
                while nums:
                    cur = nums.popleft()
                    for neighbor in adj[cur]:
                        if dp[cur] + 1 < dp[neighbor]:
                            dp[neighbor] = dp[cur] + 1
                            nums.append(neighbor)
            res.append(dp[n - 1])
        return res

# 暴力BFS
class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        adj = [[] for _ in range(n)]
        for i in range(n - 1):
            adj[i].append(i + 1)

        def bfs():
            nums = deque([0])
            vis = [False] * n
            cost = [0] * n
            while nums:
                cur = nums.popleft()
                if cur == n - 1:
                    break
                else:
                    for i in adj[cur]:
                        if not vis[i]:
                            vis[i] = True
                            nums.append(i)
                            cost[i] = cost[cur] + 1
            return cost[n - 1]

        res = []
        for i, j in queries:
            adj[i].append(j)
            res.append(bfs())
        return res
