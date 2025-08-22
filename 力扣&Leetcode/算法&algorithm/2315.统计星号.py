class Solution:
    def countAsterisks(self, s: str) -> int:
        res = s.split("|")
        ans = 0
        for i in range(len(res)):
            if i % 2 == 0:
                ans += res[i].count("*")
        return ans
