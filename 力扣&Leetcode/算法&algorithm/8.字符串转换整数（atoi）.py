class Solution:
    def myAtoi(self, s: str) -> int:
        res = []
        nums = [i for i in s]
        while nums != [] and nums[0] == " ":
            del nums[0]
        if not nums:
            return 0
        swap = True
        if len(nums) > 0 and nums[0] == "-":
            swap = False
            del nums[0]
        for idx, i in enumerate(nums):
            if i == "+":
                if idx == 0 and swap:
                    continue
                else:
                    break
            elif i.isdigit():
                res.append(i)
            elif not i.isdigit():
                break
        if not res:
            return 0
        ans = int("".join(res))
        if not swap:
            ans *= -1
        if ans > 2**31 - 1:
            return 2**31 - 1
        elif ans < -(2**31):
            return -(2**31)
        else:
            return ans
