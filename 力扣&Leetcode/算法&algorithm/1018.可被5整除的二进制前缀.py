class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        a = []
        for i in range(len(nums)):
            a += str(nums[i])
            ans = int("".join(list(a)), 2)
            if ans % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res
