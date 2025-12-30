class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        cnt = {0: 0, 1: 0}
        for i in position:
            cnt[i % 2] += 1
        return min(cnt.values())
