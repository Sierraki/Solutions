class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a = [0] * (len(arr) - 1) + [-1]
        mx = 0
        for i in range(len(arr) - 2, -1, -1):
            mx = max(mx, arr[i + 1])
            a[i] = mx
        return a
