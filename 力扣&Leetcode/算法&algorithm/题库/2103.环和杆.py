class Solution:
    def countPoints(self, rings: str) -> int:
        cnt = defaultdict(set)
        ans = 0
        for i in range(1, len(rings), 2):
            cnt[rings[i]].add(rings[i - 1])
        for i in cnt.values():
            if len(i) == 3:
                ans += 1
        return ans
