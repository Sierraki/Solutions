class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def fun(a=list, b=list, c=list) -> bool:
            x1, y1 = a[0], a[1]
            x2, y2 = b[0], b[1]
            x3, y3 = c[0], c[1]
            return (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)

        for i in range(2, len(coordinates)):
            if not fun(coordinates[i - 2], coordinates[i - 1], coordinates[i]):
                return False
        return True
