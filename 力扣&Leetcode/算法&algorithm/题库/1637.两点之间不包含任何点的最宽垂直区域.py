from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        a = [i[0] for i in points]
        a.sort()
        mx = 0
        for i in range(1, len(points)):
            mx = max(mx, a[i] - a[i - 1])
        return mx
