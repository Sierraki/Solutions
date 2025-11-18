class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        bi = Counter(birth)
        de = Counter(death)
        ans = 1900
        lived = 0
        cur = 0
        for i in range(1900, 2001):
            cur += bi[i] - de[i - 1]
            if cur > lived:
                ans = i
                lived = cur
        return ans
