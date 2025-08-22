class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        mx = -float("inf")
        ans = -float("inf")
        for i in dimensions:
            if sqrt(i[0] ** 2 + i[1] ** 2) > mx:
                mx = sqrt(i[0] ** 2 + i[1] ** 2)
                ans = i[0] * i[1]
            if sqrt(i[0] ** 2 + i[1] ** 2) == mx:
                ans = max(ans, i[0] * i[1])
        return ans
