class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        a = []
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                a.append(nums[left] ** 2)
                left += 1
            else:
                a.append(nums[right] ** 2)
                right -= 1
        retur(a[::-1])
