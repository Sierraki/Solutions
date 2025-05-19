class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:

        n = len(startTime)
        a = [startTime[i] - endTime[i - 1] for i in range(1, n)]

        if eventTime > endTime[-1]:
            a.append(eventTime - endTime[-1])
        if 0 < startTime[0]:
            a.insert(0, startTime[0])
        j = k + 1
        cur = sum(a[:j])

        big = cur

        for i in range(j, len(a)):
            cur += a[i] - a[i - j]
            big = max(big, cur)
        return big
