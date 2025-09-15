class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums1 = nums.copy()
        nums.sort()
        # search left
        res = Counter()
        for i in nums:
            lc = bisect.bisect_left(nums, i)
            if i not in res:
                res[i] += lc
        ans = []
        for i in nums1:
            ans.append(res[i])
        return ans
