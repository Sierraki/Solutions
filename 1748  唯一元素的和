class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        cur = 0
        for i, j in cnt.items():
            if j == 1:
                cur += i
        return cur


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        a = []
        b = []
        for i in nums:
            if i in b and i in a:
                a.remove(i)
            elif i in a and i not in b:
                a.remove(i)
                b.append(i)
            elif i not in a and i not in b:
                a.append(i)
            elif i not in a and i in b:
                continue
        return sum(a)
