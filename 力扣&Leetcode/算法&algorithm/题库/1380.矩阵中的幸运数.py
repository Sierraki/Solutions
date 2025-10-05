class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # revolve
        res = []
        for i in range(len(matrix[0])):
            cur = []
            for j in range(len(matrix)):
                cur.append(matrix[j][i])
            res.append(cur)
        mi = []
        for i in res:
            mi.append(max(i))
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min(matrix[i]) and matrix[i][j] == mi[j]:
                    ans.append(matrix[i][j])
        return ans
