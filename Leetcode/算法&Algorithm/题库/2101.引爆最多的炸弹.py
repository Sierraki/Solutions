class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        def check(x1, y1, r1, x2, y2):
            return ((y1 - y2) ** 2 + (x1 - x2) ** 2) <= r1**2

        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                a = bombs[i]
                b = bombs[j]
                if check(a[0], a[1], a[2], b[0], b[1]):
                    adj[i].append(j)
                if check(b[0], b[1], b[2], a[0], a[1]):
                    adj[j].append(i)

        def dfs(cur):
            vis.add(cur)
            cnt[0] += 1
            for i in adj[cur]:
                if i not in vis:
                    dfs(i)

        mx = -float("inf")
        for i in range(n):
            cnt = [0]
            vis = set()
            dfs(i)
            mx = max(mx, cnt[0])
        return mx
