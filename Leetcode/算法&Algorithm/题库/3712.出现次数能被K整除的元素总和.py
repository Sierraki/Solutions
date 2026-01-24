class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        ans = 0
        for i, j in cnt.items():
            if j % k == 0:
                ans += i * j
        return ans
