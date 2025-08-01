class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        cnt = Counter()
        cnt[logs[0][0]] = logs[0][1]
        for i in range(1, len(logs)):
            cnt[logs[i][0]] = max(logs[i][1] - logs[i - 1][1], cnt[logs[i][0]])
        tar = max(cnt.values())
        ans = float("inf")
        for i in cnt.keys():
            if cnt[i] == tar:
                ans = min(i, ans)
        return ans
