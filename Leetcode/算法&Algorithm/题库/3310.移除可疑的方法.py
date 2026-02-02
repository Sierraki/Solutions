class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        nums = [[] for _ in range(n)]
        for i, j in invocations:
            nums[i].append(j)
        vis = [False] * n
        res = set()

        def dfs(cur):
            if not vis[cur]:
                vis[cur] = True
                res.add(cur)
                for i in nums[cur]:
                    if not vis[i]:
                        dfs(i)

        dfs(k)
        res1 = set([i for i in range(n) if i not in res])
        for i, j in invocations:
            if j in res and i in res1:
                return list(res1) + list(res)
        return list(res1)
