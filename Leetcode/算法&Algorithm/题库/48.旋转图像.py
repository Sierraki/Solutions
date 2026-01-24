class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in matrix:
            l, r = 0, n - 1
            while l <= r:
                i[l], i[r] = i[r], i[l]
                l += 1
                r -= 1
