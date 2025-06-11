class Solution:
    def isBalanced(self, num: str) -> bool:
        odd = even = 0
        for idx, i in enumerate(num):
            if idx % 2 == 0:
                even += int(i)
            else:
                odd += int(i)
        return odd == even
