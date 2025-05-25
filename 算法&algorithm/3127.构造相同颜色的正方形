class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        block1 = [
            grid[0][0],
            grid[0][1],
            grid[1][0],
            grid[1][1],
        ]
        block2 = [
            grid[0][1],
            grid[0][2],
            grid[1][1],
            grid[1][2],
        ]
        block3 = [
            grid[1][0],
            grid[1][1],
            grid[2][0],
            grid[2][1],
        ]
        block4 = [
            grid[1][1],
            grid[1][2],
            grid[2][1],
            grid[2][2],
        ]
        nums = [block1, block2, block3, block4]
        for i in nums:
            cnt = Counter(i)
            if cnt["B"] <= 1 or cnt["W"] <= 1:
                return True
        else:
            return False
