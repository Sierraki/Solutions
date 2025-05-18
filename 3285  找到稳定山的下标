class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        a = []
        for i in range(1, len(height)):
            if height[i - 1] > threshold:
                a.append(i)
        return a
