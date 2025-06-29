class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
        lc1 = bisect.bisect_left(scores, target)
        lc2 = bisect.bisect(scores, target)
        return lc2 - lc1
