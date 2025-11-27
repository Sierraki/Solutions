class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        res = copy.deepcopy(board)
        m = len(res)
        n = len(res[0])

        def fun(a=int, b=int) -> int:
            cnt = 0
            for i in [a - 1, a, a + 1]:
                for j in [b - 1, b, b + 1]:
                    if 0 <= i < m and 0 <= j < n and [i, j] != [a, b]:
                        cnt += res[i][j]
            return cnt

        for i in range(m):
            for j in range(n):
                tar = fun(i, j)
                if tar < 2:
                    board[i][j] = 0
                elif tar <= 3:
                    if tar == 3:
                        board[i][j] = 1
                elif tar > 3:
                    board[i][j] = 0
