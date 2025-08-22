class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        pin = 1
        while pin < len(arr):
            if arr[pin] >= arr[pin + 1]:
                return pin
            pin += 1
