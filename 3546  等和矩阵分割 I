class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        su = 0
        st = False
        for i in grid:
            for j in i:
                su += j
        # print(su)
        target = su / 2
        # print(target)
        row = []
        for i in grid:
            row.append(sum(i))
        # print(row)
        col = []
        for i in range(len(grid[0])):  # 单个长度
            s = 0
            for j in range(len(grid)):  # 遍历整个grid
                s += grid[j][i]
            col.append(s)
        # print(col)
        # return(su)

        # row
        t = su
        for i in row:
            t -= i
            if target == t:
                st = True

        # col
        t = su
        for i in col:
            t -= i
            if target == t:
                st = True
        return st
