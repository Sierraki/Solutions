class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        h = False
        b = False

        if (
            length >= 10**4
            or width >= 10**4
            or height >= 10**4
            or length * width * height >= 10**9
        ):
            b = True
        if mass >= 100:
            h = True
        if b and h:
            return "Both"
        elif not b and not h:
            return "Neither"
        elif h and not b:
            return "Heavy"
        elif b and not h:
            return "Bulky"
