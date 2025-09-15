class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        hex_chars = "0123456789abcdef"
        res = ""
        # 处理负数，按32位无符号整数处理
        num &= 0xFFFFFFFF
        while num:
            res = hex_chars[num % 16] + res
            num //= 16
        return res
