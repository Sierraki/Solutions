class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        ans = -1
        for idx, i in enumerate(nums):
            if idx == i:
                if ans == -1:
                    ans = idx
                else:
                    ans = min(ans, idx)
        return ans
