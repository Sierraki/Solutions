from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect, bisect_left
from collections import deque
from typing import List, Optional
from fractions import Fraction


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


def locate(i=int, j=int) -> int:
    m = ceil(i // 3)
    n = ceil(j // 3)
    return (m) * 3 + n


col = defaultdict(list)
row = defaultdict(list)
box = defaultdict(list)


def fun(board) -> bool:
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


print(fun(board))
print(dict(col))
print(dict(row))
print(dict(box))
