class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        tar = sum(nums) / len(nums)
        cnt = Counter(nums)
        ans = floor(tar) + 1
        while ans in cnt or ans <= 0:
            ans += 1
        return ans
