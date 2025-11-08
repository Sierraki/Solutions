class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            tar_cnt = 0
            for j in range(i, n):
                if nums[j] == target:
                    tar_cnt += 1
                length = j - i + 1
                if tar_cnt > length // 2:
                    ans += 1
        return ans
