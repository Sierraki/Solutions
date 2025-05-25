class Solution:
    def isHappy(self, n: int) -> bool:
        a = []
        if n == 1:
            return True
        else:
            while n != 1:
                s = 0
                for i in str(n):
                    s = s + int(i) ** 2
                    n = s
                if n in a and a != 1:
                    return False
                    break
                if n not in a and a != 1:
                    a.append(n)
                if n == 1:
                    return True
                    break
