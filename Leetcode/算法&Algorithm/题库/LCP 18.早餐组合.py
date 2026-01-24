class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        mod = 10**9 + 7
        drinks.sort()
        ans = 0
        for i in staple:
            tar = x - i
            lc = bisect.bisect(drinks, tar)
            ans += lc
        return ans % mod
