class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * n

        def backtrack(path=list[int]):
            if len(path) == n:
                res.append(path.copy())
                return
            for i in range(n):
                if used[i] == False:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(path)
                    used[i] = False
                    path.pop()

        backtrack([])
        return res
