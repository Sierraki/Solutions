class Solution:
    def reconstructMatrix(
        self, upper: int, lower: int, colsum: List[int]
    ) -> List[List[int]]:
        if sum(colsum) != upper + lower:
            return []
        cnt2 = colsum.count(2)
        if not (cnt2 <= min(upper, lower)):
            return []
        res = [[i, j] for i, j in enumerate(colsum) if j == 1]
        n = len(colsum)
        ans = [[0] * n for _ in range(2)]
        for i, j in enumerate(colsum):
            if j == 2:
                ans[0][i] = ans[1][i] = 1
        res1 = upper - cnt2
        for i in range(res1):
            ans[0][res[-1][0]] = 1
            res.pop()
        for i, j in res:
            ans[1][i] = 1
        return ans
