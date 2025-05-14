class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        cur = 0
        while mainTank >= 5 and additionalTank >= 0:
            mainTank -= 5
            cur += 50
            additionalTank -= 1
            if additionalTank < 0:
                break
            mainTank += 1
        cur += mainTank * 10
        return cur
