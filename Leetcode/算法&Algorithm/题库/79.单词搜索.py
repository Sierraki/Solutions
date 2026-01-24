class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def fun(r, c, pin):
            if pin == len(word):
                return True
            if not (0 <= r < m and 0 <= c < n) or board[r][c] != word[pin]:
                return False
            tmp = board[r][c]
            board[r][c] = "@"
            res = (
                fun(r - 1, c, pin + 1)
                or fun(r + 1, c, pin + 1)
                or fun(r, c - 1, pin + 1)
                or fun(r, c + 1, pin + 1)
            )
            board[r][c] = tmp
            return res

        for i in range(m):
            for j in range(n):
                if fun(i, j, 0):
                    return True
        return False

from collections import Counter
from itertools import chain


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # --- 优化 A: 长度检查 ---
        if len(word) > rows * cols:
            return False

        # --- 优化 B: 词频统计剪枝 ---
        board_counts = Counter(chain(*board))
        word_counts = Counter(word)
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False

        # --- 优化 C: 改变搜索顺序 ---
        # 如果末尾字符在棋盘中更少，反转单词从末尾开始搜，分支会少很多
        if board_counts[word[-1]] < board_counts[word[0]]:
            word = word[::-1]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = "#"  # 标记

            # 依次尝试四个方向
            if (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            ):
                return True

            board[r][c] = temp  # 回溯
            return False

        # 启动 DFS
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False
