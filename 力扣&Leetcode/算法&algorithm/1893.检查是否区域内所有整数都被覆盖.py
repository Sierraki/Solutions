class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cnt = Counter()
        for i in range(left, right + 1):
            cnt[i] += 1
        for i, j in ranges:
            for k in range(i, j + 1):
                cnt[k] -= 1
        return max(cnt.values()) <= 0
