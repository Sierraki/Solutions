class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        p = {"6": "9", "1": "1", "0": "0", "8": "8", "9": "6"}
        n = len(num)
        l = 0
        r = n - 1
        stat = True
        for i in num:
            if i not in p:
                stat = False
        while l <= r and stat:
            if num[l] == p[num[r]]:
                l += 1
                r -= 1
            else:
                stat = False
        return stat
