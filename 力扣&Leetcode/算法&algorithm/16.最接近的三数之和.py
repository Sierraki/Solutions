class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mi = float("inf")
        res = float("inf")
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                ans = nums[i] + nums[l] + nums[r]
                if ans > target:
                    if abs(ans - target) < mi:
                        mi = abs(ans - target)
                        res = ans
                    r -= 1
                elif ans < target:
                    if abs(ans - target) < mi:
                        mi = abs(ans - target)
                        res = ans
                    l += 1
                else:
                    res = ans
                    break
        return res
