class Solution:
    def similarRGB(self, color: str) -> str:
        def fun(ori=str) -> str:
            val = int("0x" + ori, 16)
            res = round(val / 17)
            tar = hex(res * 17)[2:]
            if len(tar) == 1:
                return tar * 2
            return tar

        ans = "#"
        for i in range(2, len(color), 2):
            ans += fun(color[i - 1 : i + 1])
        return ans
