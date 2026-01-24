class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()

        def bt(start, path):
            if len(path) == k:
                res.add("/".join(map(str, sorted(path.copy()))))
                return
            for i in range(start, n):
                path.append(nums[i])
                bt(i + 1, path)
                path.pop()

        for k in range(n + 1):
            bt(0, [])
        res = list(res)
        for i in range(len(res)):
            if res[i]:
                res[i] = list(map(int, res[i].split("/")))
            else:
                res[i] = []
        return res
