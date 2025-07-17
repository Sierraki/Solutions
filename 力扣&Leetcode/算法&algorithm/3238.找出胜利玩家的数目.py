class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        cnt = defaultdict(list)
        for i in pick:
            cnt[i[0] + 1].append(i[1])
        ans = 0
        for i, j in cnt.items():
            if max(Counter(j).values()) >= i:
                ans += 1
        return ans
