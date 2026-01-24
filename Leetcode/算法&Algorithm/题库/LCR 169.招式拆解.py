class Solution:
    def dismantlingAction(self, arr: str) -> str:
        cnt = Counter(arr)
        for i, j in cnt.items():
            if j == 1:
                return i
        return " "
