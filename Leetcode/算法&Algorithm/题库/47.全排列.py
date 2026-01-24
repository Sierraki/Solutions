class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        used = [False] * n

        def backtrack(path):
            if len(path) == n:
                ans = "/".join(map(str, path.copy()))
                res.add(ans)
                return
            for i in range(n):
                if used[i] == False:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(path)
                    used[i] = False
                    path.pop()

        backtrack([])

        return [list(map(int, i.split("/"))) for i in res]
