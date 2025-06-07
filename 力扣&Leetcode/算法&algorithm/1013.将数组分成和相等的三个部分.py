class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        tar = sum(arr) / 3
        left, right = 0, len(arr) - 1
        sl, sr = 0, 0
        lc1, lc2 = -1, -1
        while left < len(arr):
            sl += arr[left]
            if sl == tar:
                lc1 = left
                break
            left += 1
        while right != 0:
            sr += arr[right]
            if sr == tar:
                lc2 = right
                break
            right -= 1
        return sl == sr == sum(arr) - sl - sr and lc2 - lc1 > 1
