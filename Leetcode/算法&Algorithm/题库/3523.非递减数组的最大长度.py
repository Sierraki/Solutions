class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        ans = []
        for i in nums:
            if not ans or (ans and i >= ans[-1]):
                ans.append(i)
        return len(ans)
