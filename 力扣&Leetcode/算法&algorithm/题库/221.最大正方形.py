class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if "1" in matrix:
            mx = 2
        else:
            mx = 1

        def check(matrix: list, a: list, b: list) -> bool:
            if b[0] - a[0] != b[1] - a[1]:
                return False
            for i in range(a[0], b[0] + 1):
                for j in range(a[1], b[1] + 1):
                    if matrix[i][j] == "0":
                        return False
            return True

        if mx == 1:
            start = 0
        if mx == 2:
            start = 1
        for i in range(start, m):
            for j in range(mx - 1, n):
                if check(matrix, [i - mx + 1, j - mx + 1], [i, j]):
                    mx += 1
                    print(mx, [i, j])
                    break
        return (mx - 1) ** 2
