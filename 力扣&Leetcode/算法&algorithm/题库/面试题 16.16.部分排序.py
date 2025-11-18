class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        if len(array) <= 1:
            return [-1, -1]
        n = len(array)
        mx = []
        mi = []
        ans = -float("inf")
        for i in range(n):
            ans = max(ans, array[i])
            mx.append(ans)
        ans = float("inf")
        for i in range(n - 1, -1, -1):
            ans = min(ans, array[i])
            mi.insert(0, ans)
        nums = []
        for i in range(n):
            if mx[i] > mi[i]:
                nums.append(i)
        if not nums:
            return [-1, -1]
        return [nums[0], nums[-1]]
