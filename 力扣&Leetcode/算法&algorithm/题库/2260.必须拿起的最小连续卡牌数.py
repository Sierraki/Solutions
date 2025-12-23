class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = float("inf")
        cnt = defaultdict()
        for i, j in enumerate(cards):
            if j in cnt:
                ans = min(ans, i - cnt[j] + 1)
            cnt[j] = i
        return ans if ans != float("inf") else -1
