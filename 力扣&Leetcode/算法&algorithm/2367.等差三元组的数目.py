class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        cnt = Counter(nums)
        ans = 0
        for i in nums:
            if i + diff in cnt and i + 2 * diff in cnt:
                ans += 1
        return ans
