class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        cnt = Counter(i for i in nums if i % 2 == 0)
        if not cnt:
            return -1
        tar = max(cnt.values())
        ans = float("inf")
        for i, j in cnt.items():
            if j == tar:
                ans = min(ans, i)
        return ans
