class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        def select(val: int, low: int, up: int):
            if low <= val <= up:
                return 0
            elif val < low:
                return low - val
            else:
                return val - up

        a = select(xCenter, x1, x2)
        b = select(yCenter, y1, y2)

        return a * a + b * b <= radius * radius
