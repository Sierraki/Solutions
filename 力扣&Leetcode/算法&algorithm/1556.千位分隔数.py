class Solution:
    def thousandSeparator(self, n: int) -> str:
        nums = [i for i in str(n)]
        res = []
        while nums:
            if len(nums) >= 3:
                a = "".join(nums[-3:])
                nums = nums[:-3]
                res.append(a)
            else:
                res.append("".join(nums))
                break
        res = res[::-1]
        if len(res) == 1:
            ans = res[0]
        else:
            ans = ""
            for i in range(len(res)):
                ans += res[i] + "."
            ans = ans[:-1]
        return ans
