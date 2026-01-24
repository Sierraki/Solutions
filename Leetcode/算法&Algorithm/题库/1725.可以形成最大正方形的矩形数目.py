class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        mx = -float("inf")
        for i in rectangles:
            mx = max(mx, min(i))
        ans = 0
        for i in rectangles:
            if min(i) >= mx:
                ans += 1
        return ans
