class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def locate(i=int, j=int) -> int:
            m = ceil(i // 3)
            n = ceil(j // 3)
            return (m) * 3 + n

        col = defaultdict(list)
        row = defaultdict(list)
        box = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row[i]:
                        return False
                    if board[i][j] in col[j]:
                        return False
                    if board[i][j] in box[locate(i, j)]:
                        return False
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
                    box[locate(i, j)].append(board[i][j])
        return True
