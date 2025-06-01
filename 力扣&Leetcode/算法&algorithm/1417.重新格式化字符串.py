class Solution:
    def reformat(self, s: str) -> str:
        alpha = []
        nums = []
        a = []
        for i in s:
            if i.isalpha():
                alpha.append(i)
            else:
                nums.append(i)
        ca = []
        if abs(len(alpha) - len(nums)) > 1:
            return ""
        if len(alpha) > len(nums):
            ca.append(alpha[-1])
            alpha.pop()
        elif len(alpha) < len(nums):
            ca.append(nums[-1])
            nums.pop()
        a = list(zip(nums, alpha))
        if ca:
            if ca[0].isalpha():
                a = ca + a
            else:
                a = a + ca
        res = []
        for i in a:
            for j in i:
                res.append(j)
        return "".join(res)
