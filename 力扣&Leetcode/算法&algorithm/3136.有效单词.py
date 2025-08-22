class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        yy = False
        fy = False
        num = False
        al = False
        e = False
        for i in word:
            if i in "aeiouAEIOU":
                yy = True
            elif i.isalpha() and i not in "aeiouAEIOU":
                fy = True
            if i.isalpha():
                al = True
            elif i.isdigit():
                num = True
            else:
                e = True
        if yy and fy and (num or al) and not e:
            return True
        return False
