class Solution:
    def check(self, nums: List[int]) -> bool:
        tar = sorted(nums)
        nums += nums
        for idx, i in enumerate(nums):
            if i == tar[0]:
                ans = nums[idx : idx + len(tar)] == tar
                if ans:
                    return True
        return False
