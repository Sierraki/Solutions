class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        def fun(nums):
            res = []
            s = 0
            for i in nums:
                s += i
                res.append(s)
            return res

        for i in range(len(matrix)):
            matrix[i] = fun(matrix[i])
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = col1
        right = col2
        top = row1
        down = row2
        ans = 0
        for i in range(top, down + 1):
            if left != 0:
                ans += self.matrix[i][right] - self.matrix[i][left - 1]
            else:
                ans += self.matrix[i][right]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
