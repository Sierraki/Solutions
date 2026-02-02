class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        nums = [[] for _ in range(n)]
        for i, j in enumerate(arr):
            if 0 <= i - j < n:
                nums[i].append(i - j)
            if 0 <= i + j < n:
                nums[i].append(i + j)
        vis = [False] * n

        def dfs(cur):
            if arr[cur] == 0:
                return True
            for i in nums[cur]:
                if vis[i] == False:
                    vis[i] = True
                    if dfs(i):
                        return True
            else:
                return False

        return dfs(start)
