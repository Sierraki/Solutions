class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [False] * (n)

        def dfs(cur):
            vis[cur] = True
            for idx, j in enumerate(isConnected[cur]):
                if j == 1 and vis[idx] == False:
                    vis[idx] = True
                    dfs(idx)

        cnt = 0
        for i in range(n):
            if vis[i] == False:
                cnt += 1
                dfs(i)
        return cnt
