class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)

        left = 0
        right = n - 1

        while left < right:
            if arr[left] <= arr[left + 1]:
                left += 1
            if arr[right - 1] >= arr[right]:
                right -= 1

        return left
