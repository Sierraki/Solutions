class Solution:
    def twoSum(self, price: List[int], target: int) -> List[int]:
        for i in price:
            tar = target - i
            lc = bisect.bisect(price, tar) - 1
            if tar == price[lc]:
                return (tar, i)
