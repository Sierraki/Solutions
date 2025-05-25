class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        a = celsius + 273.15
        b = celsius * 1.8 + 32
        return [a, b]
