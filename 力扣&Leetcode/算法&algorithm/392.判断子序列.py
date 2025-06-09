class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        check = []
        if not s:
            return True
        pin = 0
        for i in t:
            if i == s[pin]:
                pin += 1
                check.append(i)
            if i in check and i != check[-1]:
                check = []
                if i == s[0]:
                    check.append(i)
                pin += 1
            if "".join(check) == s:
                return True
                break
        return False
