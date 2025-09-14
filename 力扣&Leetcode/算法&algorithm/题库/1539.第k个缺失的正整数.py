class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res = [i for i in range(1, max(arr) + 1) if i not in arr]
        for i in res:
            k -= 1
            if k == 0:
                ans = i
        if k > 0:
            ans = max(arr) + k
        return ans


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k
