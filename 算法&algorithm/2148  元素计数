class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        r = n - 1
        cnt = 2
        if len(set(nums)) <= 2:
            return 0
        else:
            while nums[l] == nums[l + 1] or nums[r - 1] == nums[r]:
                if nums[l] == nums[l + 1]:
                    l += 1
                    cnt += 1
                elif nums[r - 1] == nums[r]:
                    r -= 1
                    cnt += 1
                else:
                    break
            return n - cnt
