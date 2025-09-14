class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        for i in range(len(grid)):
            if i % 2 == 1:
                grid[i] = grid[i][::-1]
        res = [j for i in grid for j in i]
        ans = []
        for i in range(len(res)):
            if i % 2 == 0:
                ans.append(res[i])
        return ans
