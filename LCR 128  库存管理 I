class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
        # 探索左边界
        left, right = 0, len(stock) - 1
        while left < right:
            mid = (left + right) // 2
            if stock[mid] > stock[right]:
                left = mid + 1
            elif stock[mid] < stock[right]:
                right = mid
            else:
                right -= 1
        return stock[left]
