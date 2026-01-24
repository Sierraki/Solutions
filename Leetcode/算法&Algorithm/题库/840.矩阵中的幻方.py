class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(nums):
            a = b = 0
            for i in range(3):
                a += nums[i][i]
                b += nums[i][2 - i]
                if nums[i][0] + nums[i][1] + nums[i][2] != 15:
                    return False
                if nums[0][i] + nums[1][i] + nums[2][i] != 15:
                    return False
            cnt = Counter([j for i in nums for j in i if 0 < j <= 9])
            if len(cnt) != 9:
                return False
            return a == b == 15

        cnt = 0
        m = len(grid)
        n = len(grid[0])
        res = []
        if m >= 3 and n >= 3:
            for r in range(m - 2):
                for c in range(n - 2):
                    cur = [
                        grid[r][c : c + 3],
                        grid[r + 1][c : c + 3],
                        grid[r + 2][c : c + 3],
                    ]
                    res.append(cur)
        for i in res:
            if check(i):
                cnt += 1
        return cnt
