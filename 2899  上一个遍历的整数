class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        wl = 0
        k = 0
        for i in nums:
            if int(i) > 0:
                seen.append(i)
                wl += 1
                k = 0
            else:
                k += 1
                if k <= wl:
                    ans.append(seen[-k])
                else:
                    ans.append(-1)
        return ans
