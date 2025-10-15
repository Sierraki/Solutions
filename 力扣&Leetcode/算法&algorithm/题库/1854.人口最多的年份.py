class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        live_cnt = Counter()
        die_cnt = Counter()
        for i, j in logs:
            live_cnt[i] += 1
            die_cnt[j] += 1
        year = [j for i in logs for j in i]
        mi = min(year)
        mx = max(year)
        alive = 0
        ans = 0
        tar = mi
        for i in range(mi, mx + 1):
            alive += live_cnt[i]
            alive -= die_cnt[i]
            if alive > ans:
                ans = alive
                tar = i
        return tar
