class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        a = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 跳过重复元素
            l = i + 1
            r = n - 1
            while l < r:
                target = 0 - nums[i]
                lr = nums[l] + nums[r]
                if lr == target:
                    a.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1  # 跳过重复元素
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1  # 跳过重复元素
                    l += 1
                    r -= 1
                elif lr < target:
                    l += 1
                else:
                    r -= 1
        return a
