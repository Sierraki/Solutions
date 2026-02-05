class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nums = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            nums[j].append(i)
        vis = [0] * numCourses

        def dfs(cur):
            if vis[cur] > 0:
                return vis[cur] == 2
            vis[cur] = 1
            for i in nums[cur]:
                if not dfs(i):
                    return False
            vis[cur] = 2
            return True

        for i in range(numCourses):
            dfs(i)
        for i in vis:
            if i < 2:
                return False
        return True
