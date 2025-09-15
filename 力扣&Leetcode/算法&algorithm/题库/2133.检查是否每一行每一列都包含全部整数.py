class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        def fun(matrix: List) -> bool:
            n = len(matrix)
            cnt = Counter()
            for i in range(1, n + 1):
                cnt[i] = 0
            for i in matrix:
                for j in i:
                    cnt[j] += 1
                if max(cnt.values()) != min(cnt.values()):
                    return False
            return True

        ans = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ans[i][j] = matrix[j][i]
        return fun(matrix) and fun(ans)
