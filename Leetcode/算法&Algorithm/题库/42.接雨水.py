class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = []
        lmx = height[0]
        rmx = height[-1]
        for i in height:
            lmx = max(lmx, i)
            left.append(lmx)
        for i in range(len(height) - 1, -1, -1):
            rmx = max(rmx, height[i])
            right.insert(0, rmx)
        ans = 0
        for i in range(1, len(height) - 1):
            if left[i] > height[i] and right[i] > height[i]:
                ans += min(left[i], right[i]) - height[i]
        return ans
