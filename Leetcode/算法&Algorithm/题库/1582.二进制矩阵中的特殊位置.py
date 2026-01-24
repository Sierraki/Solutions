class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row = [sum(i) for i in mat]
        col = []
        for i in range(len(mat[0])):
            a = 0
            for j in range(len(mat)):
                a += mat[j][i]
            col.append(a)
        res = 0
        for i in range(len(row)):
            for j in range(len(col)):
                if row[i] == col[j] == 1 and mat[i][j] == 1:
                    res += 1
        return res
