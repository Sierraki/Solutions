class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        cur = 0
        left = 0
        while left < n:
            # 如果当前字符小于下一个字符，说明是特殊情况
            if left < n - 1 and dict1[s[left]] < dict1[s[left + 1]]:
                cur += dict1[s[left + 1]] - dict1[s[left]]
                left += 2  # 跳过两个字符
            else:
                cur += dict1[s[left]]
                left += 1  # 正常处理一个字符
        return cur
