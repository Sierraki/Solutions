class Solution:
    def minTimeToType(self, word: str) -> int:
        # 最小路径
        def fun(start: str, tar: str) -> int:
            a = ord(tar) - ord(start)
            b = 26 - abs(ord(tar) - ord(start))
            if start == tar:
                return 1
            return min(abs(a), abs(b)) + 1

        ans = 0
        if word[0] != "a":
            ans += fun("a", word[0])
        else:
            ans += 1
        for i in range(1, len(word)):
            ans += fun(word[i - 1], word[i])
        return ans
