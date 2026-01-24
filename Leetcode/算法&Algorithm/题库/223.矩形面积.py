class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        def fun(a1: int, a2: int, b1: int, b2: int) -> int:
            if a2 <= b1 or b2 <= a1:
                return 0
            elif b1 <= a1 <= a2 <= b2:
                return a2 - a1
            elif a1 <= b1 <= b2 <= a2:
                return b2 - b1
            elif a1 <= b1 <= a2 <= b2:
                return a2 - b1
            else:
                return b2 - a1

        return (
            abs(ay2 - ay1) * abs(ax2 - ax1)
            + abs(by2 - by1) * abs(bx2 - bx1)
            - fun(ax1, ax2, bx1, bx2) * fun(ay1, ay2, by1, by2)
        )
