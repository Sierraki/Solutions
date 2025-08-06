class Solution:
    def findIndices(
        self, nums: List[int], indexDifference: int, valueDifference: int
    ) -> List[int]:
        # index
        l, r = 0, indexDifference
        vmx = vmi = nums[0]
        imx = imi = 0
        ans = [-1, -1]
        while l <= r and r < len(nums):
            # 左边取最小
            if nums[l] < vmi:
                imi = l
                vmi = nums[l]
            # 左边取最大
            if nums[l] > vmx:
                imx = l
                vmx = nums[l]
            if abs(nums[r] - vmi) >= valueDifference:
                ans = [r, imi]
                break
            elif abs(nums[r] - vmx) >= valueDifference:
                ans = [r, imx]
                break
            r += 1
            l += 1
        return ans
