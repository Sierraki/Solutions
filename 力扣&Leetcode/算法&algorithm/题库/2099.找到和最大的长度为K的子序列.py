class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        res = sorted(nums, reverse=True)
        cnt = Counter(res[:k])
        ans = []
        for i in nums:
            if i in cnt:
                ans.append(i)
                cnt[i] -= 1
                if cnt[i] == 0:
                    del cnt[i]
                if len(ans) == k:
                    return ans
