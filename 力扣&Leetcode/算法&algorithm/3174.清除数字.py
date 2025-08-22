class Solution:
    def clearDigits(self, s: str) -> str:
        al = []
        for i in s:
            if i.isalpha():
                al.append(i)
            elif i.isdigit():
                al.pop()
        return "".join(al)
