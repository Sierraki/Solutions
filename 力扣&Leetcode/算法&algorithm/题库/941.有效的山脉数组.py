class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        left = 0
        while left + 1 < n and arr[left] < arr[left + 1]:
            left += 1
        if left == 0 or left == n - 1:
            return False
        while left + 1 < n and arr[left] > arr[left + 1]:
            left += 1
        return left == n - 1
