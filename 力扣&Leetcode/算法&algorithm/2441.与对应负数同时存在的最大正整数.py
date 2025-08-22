class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        po = [i for i in nums if i > 0]
        ne = {i for i in nums if i < 0}
        ans = -1
        for i in po:
            if -i in ne:
                ans = max(i, ans)
        return ans
