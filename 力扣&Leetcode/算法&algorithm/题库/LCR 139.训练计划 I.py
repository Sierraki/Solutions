from typing import List


class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        odd = [i for i in actions if i % 2 == 0]
        even = [i for i in actions if i % 2 == 1]
        return even + odd
