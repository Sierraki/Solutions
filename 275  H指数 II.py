class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        # 搜索左边界
        while left <= right:
            mid = (left + right) // 2
            target = n - mid  # 论文数量
            if target <= citations[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return n - left
