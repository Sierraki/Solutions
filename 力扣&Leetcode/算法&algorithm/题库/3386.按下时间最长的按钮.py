class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        cnt = Counter()
        cnt[events[0][0]] = events[0][1]
        for i in range(1, len(events)):
            cnt[events[i][0]] = max(cnt[events[i][0]], events[i][1] - events[i - 1][1])
        return min([i for i in cnt.keys() if cnt[i] == max(cnt.values())])
