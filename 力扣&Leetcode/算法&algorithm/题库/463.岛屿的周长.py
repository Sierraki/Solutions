from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cnt = 0
        col = []
        for i in range(len(grid[0])):
            a = []
            for j in grid:
                if j[i] == 1:
                    cnt += 1
                a.append(j[i])
            col.append(a)
        # print(col)
        lap = 0
        for i in grid:
            for j in range(len(i) - 1):
                if i[j] == i[j + 1] == 1:
                    lap += 1
        for i in col:
            for j in range(len(i) - 1):
                if i[j] == i[j + 1] == 1:
                    lap += 1
        lap *= 2
        return cnt * 4 - lap
