class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ans = 0
        for idx, i in enumerate(nums):
            a = idx - k
            b = idx + k
            if 0 <= a <= b <= len(nums) - 1:
                if i > nums[a] and i > nums[b]:
                    ans += i
            else:
                if 0 <= a <= len(nums) - 1:
                    if i > nums[a]:
                        ans += i
                elif 0 <= b <= len(nums) - 1:
                    if i > nums[b]:
                        ans += i
        return ans
