class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        cnt = 1
        lay = 0
        while cnt <= n**2 or lay > n:
            # -->
            for i in range(lay, n - lay - 1):
                res[lay][i] = cnt
                cnt += 1
            #  down
            for i in range(lay, n - lay - 1):
                res[i][-lay - 1] = cnt
                cnt += 1
            # left
            for i in range(-lay - 1, lay - n, -1):
                res[-lay - 1][i] = cnt
                cnt += 1
            # top
            for i in range(-lay - 1, lay - n, -1):
                res[i][lay] = cnt
                cnt += 1
            lay += 1
            if lay > n:
                break
        if n % 2 == 1:
            res[n // 2][n // 2] = cnt
        return res
