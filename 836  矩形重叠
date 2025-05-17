class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x = [[rec1[0], rec1[2]], [rec2[0], rec2[2]]]
        y = [[rec1[1], rec1[3]], [rec2[1], rec2[3]]]
        x.sort()
        y.sort()
        if x[0][-1] <= x[1][0]:
            return False
        else:
            if y[0][-1] > y[1][0]:
                return True
            else:
                return False
