class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        # 逆时针旋转90
        res = []
        for i in range(n - 1, -1, -1):
            a = []
            for j in range(m):
                a.append(matrix[j][i])
            res.append(a)
        mx = []
        for i in res:
            mx.append(max(i))
        for i in range(n):
            for j in range(m):
                if res[i][j] == -1:
                    res[i][j] = mx[i]
        res = res[::-1]
        ans = []
        for i in range(m):
            a = []
            for j in range(n):
                a.append(res[j][i])
            ans.append(a)
        return ans
