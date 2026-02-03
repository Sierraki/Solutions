class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        nums = [[] for _ in range(n)]
        res = []
        for i, j in edges:
            nums[i].append(j)
            nums[j].append(i)
        vis = [False] * n
        ans = 0

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
                res.append(path[:])

        def check(arr):
            for i in arr:
                if len(nums[i]) == len(arr) - 1:
                    continue
                else:
                    return False
            return True

        for i in res:
            if check(i):
                ans += 1
        return ans
