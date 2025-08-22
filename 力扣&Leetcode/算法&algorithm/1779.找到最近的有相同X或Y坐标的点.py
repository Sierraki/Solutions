class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = -1
        res = float("inf")
        for idx, i in enumerate(points):
            a = abs(x - i[0]) + abs(y - i[1])
            if a < res and (x == i[0] or y == i[1]):
                res = a
                ans = idx
        return ans
