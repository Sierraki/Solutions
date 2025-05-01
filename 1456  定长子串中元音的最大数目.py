class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        yy = ["a", "e", "i", "o", "u"]

        cnt = 0
        for i in range(k):

            if s[i] in yy:
                cnt += 1

        maxx = cnt  # 1
        cur = cnt

        # print(s)
        for j in range(k, len(s)):

            if s[j] in yy:
                cur += 1
            if s[j - k] in yy:
                cur -= 1

            if cur > maxx:
                maxx = cur
            # print(s[j - k], s[j], cur, maxx)

        return maxx
