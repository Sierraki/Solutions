class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def fun(cur, total, start):
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return
            for i in range(start, n):
                total += candidates[i]
                cur.append(candidates[i])
                fun(cur, total, i)
                total -= candidates[i]
                cur.pop()

        fun([], 0, 0)
        return res
