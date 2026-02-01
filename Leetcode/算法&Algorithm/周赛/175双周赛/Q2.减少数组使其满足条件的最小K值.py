class Solution:
    def minimumK(self, nums: List[int]) -> int:

        def check(k):
            if k == 0:
                return False
            cnt = 0
            for x in nums:
                cnt += (x + k - 1) // k
            return cnt <= k * k

        left = 1
        right = max(max(nums), len(nums))
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
