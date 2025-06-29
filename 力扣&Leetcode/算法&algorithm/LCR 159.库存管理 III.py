class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        stock.sort()
        if cnt > len(stock):
            return stock
        return stock[:cnt]
