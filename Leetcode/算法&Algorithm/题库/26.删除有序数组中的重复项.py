class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        lens = len(nums)
        cnt = 1
        for right in range(1, lens):
            if nums[right] != nums[left]:  # 发现重复
                cnt += 1
                nums[cnt - 1] = nums[right]
            left += 1
        return cnt
