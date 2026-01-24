class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        mi = float("inf")
        cnt = defaultdict(list)
        arr.sort()
        for i in range(1, len(arr)):
            cnt[arr[i] - arr[i - 1]].append([arr[i - 1], arr[i]])
            mi = min(mi, arr[i] - arr[i - 1])
        return cnt[mi]
