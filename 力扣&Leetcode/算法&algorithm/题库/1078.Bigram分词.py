class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = text.split()
        ans = []
        for i in range(len(res) - 2):
            if res[i] == first and res[i + 1] == second:
                ans.append(res[i + 2])
        return ans
