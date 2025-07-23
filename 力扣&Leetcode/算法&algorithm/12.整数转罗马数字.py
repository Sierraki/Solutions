class Solution:
    def intToRoman(self, num: int) -> str:
        # 分层
        # # 千分位
        def fun1(a: int) -> str:
            return "M" * (a // 1000)

        # 百分位
        def fun2(a: int) -> str:
            if a <= 300:
                return "C" * (a // 100)
            elif a == 400:
                return "CD"
            elif a <= 800:
                return "D" + "C" * ((a - 500) // 100)
            else:
                return "CM"

        # 十分位
        def fun3(a: int) -> str:
            if a <= 30:
                return "X" * (a // 10)
            elif a == 40:
                return "XL"
            elif a <= 80:
                return "L" + "X" * ((a - 50) // 10)
            elif a == 90:
                return "XC"

        # 个位
        ff = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X",
        }
        ans = []
        for idx, i in enumerate(str(num)):
            tar = int(i) * 10 ** (len(str(num)) - idx - 1)

            if tar >= 1000:
                ans.append(fun1(tar))
            elif tar >= 100:
                ans.append(fun2(tar))
            elif tar >= 10:
                ans.append(fun3(tar))
            elif tar >= 1:
                ans.append(ff[tar])
        return "".join(ans)
