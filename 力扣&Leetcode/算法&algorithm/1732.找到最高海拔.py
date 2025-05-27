from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = mx = 0
        for i in gain:
            cur += i
            mx = max(mx, cur)
        return mx
