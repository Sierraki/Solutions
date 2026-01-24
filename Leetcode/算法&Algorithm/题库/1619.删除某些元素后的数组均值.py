class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        dif = ceil(n * 0.05)
        res = arr[:-dif]
        res = res[dif:]
        return sum(res) / len(res)
