class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for i in fruits:
            for j in range(len(baskets)):
                if baskets[j] >= i:
                    del baskets[j]
                    break
        return len(baskets)
