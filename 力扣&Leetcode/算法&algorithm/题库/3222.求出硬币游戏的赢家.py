class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        y = y // 4
        if y <= x:
            if y % 2 == 0:
                return "Bob"
            else:
                return "Alice"
        else:
            if x % 2 == 0:
                return "Bob"
            else:
                return "Alice"
