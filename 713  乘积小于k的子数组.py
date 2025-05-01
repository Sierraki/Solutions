class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cnt = left = 0
        cur = 1
        if k <= 1:
            return 0
        else:

            for idx, i in enumerate(nums):
                cur *= i
                if cur < k:
                    cnt += idx - left + 1
                else:
                    while cur >= k:
                        cur /= nums[left]
                        left += 1
                        if cur < k:
                            cnt += idx - left + 1
            return cnt
