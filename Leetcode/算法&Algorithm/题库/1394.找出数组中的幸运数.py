class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        ans = -1
        for i, j in cnt.items():
            if i == j:
                ans = max(ans, i)
        return ans
