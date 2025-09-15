class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l1 = []
        for i in accounts:
            a = sum(i)
            l1.append(a)
        return max(l1)
