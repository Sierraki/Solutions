class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        self.n = n
        self.commands = commands
        cnt = 0
        for i in self.commands:
            if i == "DOWN":
                cnt += n
            elif i == "RIGHT":
                cnt += 1
            elif i == "UP":
                cnt -= n
            elif i == "LEFT":
                cnt -= 1
        return cnt
