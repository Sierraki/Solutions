class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        for i in range(n):
            nl = 1
            while i + nl <= n:
                for j in arr[i : i + nl]:
                    res += j
                nl += 2
        return res
