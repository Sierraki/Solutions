from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        # 构建列矩阵
        col = []
        for i in range(len(grid[0])):
            a = []
            for j in range(len(grid)):
                a.append(grid[j][i])
            col.append(a)
        # 统计所有正方体数量
        cnt = 0
        for i in grid:
            for j in i:
                cnt += j
        # 计算重合的面积 平面
        # 重合数量-1*2
        lap = 0
        for i in grid:
            for j in range(1, len(i)):
                lap += min(i[j], i[j - 1])
        for i in col:
            for j in range(1, len(i)):
                lap += min(i[j], i[j - 1])
        lap *= 2
        # print(lap)
        vlap = 0
        for i in grid:
            for j in i:
                ans = (j - 1) * 2
                if ans < 0:
                    ans = 0
                vlap += ans
        # print(vlap)
        res = cnt * 6 - lap - vlap
        return res
