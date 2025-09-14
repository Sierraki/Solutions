class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        if len(set(arr)) == 1:
            return int(arr[0])
        n = len(arr)
        a = arr[-1] - arr[0]
        b = a / n
        for i in range(n - 1):
            if arr[i] + b != arr[i + 1]:
                return int(arr[i] + b)
