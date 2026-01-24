class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def bt(start, path):
            if len(path) == k:
                res.append((path.copy()))
                return
            for i in range(start, n):
                path.append(nums[i])
                bt(i + 1, path)
                path.pop()

        for k in range(n + 1):
            bt(0, [])
        return res
