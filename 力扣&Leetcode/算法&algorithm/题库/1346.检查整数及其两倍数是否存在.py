class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        st = False
        a = set()
        for i in arr:
            if i in a:
                st = True
            if i % 2 == 0:
                a.add(i // 2)
            a.add(i * 2)
        return st
