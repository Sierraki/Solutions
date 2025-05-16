# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        ans = -1
        left, right = 0, n
        # 搜左边界
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid) == True:  # 目标在左，收缩右边界
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
