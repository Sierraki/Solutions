class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            return True
        else:
            for i in range(1, m):
                if n == 1:
                    return True
                else:
                    for j in range(1, n):
                        if matrix[i][j] != matrix[i - 1][j - 1]:
                            return False
        return True
