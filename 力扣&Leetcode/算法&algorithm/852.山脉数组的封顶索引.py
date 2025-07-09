class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        if len(arr) == 3:
            return arr[1]
        else:
            while l <= r:
                m = (l + r) // 2 + 1
                if arr[m - 1] < arr[m] and arr[m] > arr[m + 1]:
                    return m
                if arr[m - 1] < arr[m] < arr[m + 1]:
                    l = m + 1
                elif arr[m - 1] > arr[m] > arr[m + 1]:
                    r = m - 1
                if l == r:
                    return l
