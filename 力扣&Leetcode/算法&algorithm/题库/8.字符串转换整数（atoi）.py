# 原始解法
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
# 自动机解法
class Solution:
    def myAtoi(self, s: str) -> int:
        states = {
            "start": {"space": "start", "sign": "signed", "num": "num"},
            "signed": {"num": "num"},
            "num": {"num": "num", "dot": "pnum"},
            "pnum": {"num": "pnum"},
        }
        cur = "start"
        res_num = 0
        sign = 1
        fraction = 0.1  # 用于处理小数位
        for char in s:
            typ = "othe r"
            # 确定输入类型
            if char == " ":
                typ = "space"
            elif char in "+-":
                typ = "sign"
            elif char.isdigit():
                typ = "num"
            elif char == ".":
                typ = "dot"
            # 状态跳转：如果当前状态下没有这种输入，直接跳到 end
            cur = states[cur].get(typ, "end")
            if cur == "end":
                break
            # 在跳转的同时处理数据
            if cur == "signed":
                if char == "-":
                    sign = -1
            elif cur == "num":
                res_num = res_num * 10 + int(char)
            elif cur == "pnum" and char.isdigit():
                res_num = res_num + int(char) * fraction
                fraction *= 0.1
        ans = res_num * sign
        if ans < -(2**31):
            return -(2**31)
        elif ans > 2**31 - 1:
            return 2**31 - 1
        return int(ans)
