class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        # 检验递减
        def fun(s: list) -> bool:
            for i in range(1, len(s)):
                if s[i - 1] <= s[i]:
                    return False
            return True

        # 从左往右找第一个递增分界点
        l = r = float("inf")
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                l = i - 1
                break
        # 从右往左找第二个递增起点
        for i in range(len(nums) - 1, -1, -1):
            # print(nums[i])
            if nums[i - 1] >= nums[i]:
                r = i
                break
        if not (l < r and l > 0 and r < len(nums) - 1 and fun(nums[l : r + 1])):
            return False
        return True
