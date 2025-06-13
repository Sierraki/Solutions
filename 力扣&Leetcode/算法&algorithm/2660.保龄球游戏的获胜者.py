class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def fun(player1: list):
            p1 = 0
            for idx, i in enumerate(player1):
                if idx == 0:
                    p1 += i
                if idx == 1:
                    if player1[idx - 1] == 10:
                        p1 += 2 * i
                    else:
                        p1 += i
                if idx > 1:
                    if player1[idx - 1] == 10 or player1[idx - 2] == 10:
                        p1 += 2 * i
                    else:
                        p1 += i
            return p1

        p1 = fun(player1)
        p2 = fun(player2)
        if p1 > p2:
            return 1
        elif p2 > p1:
            return 2
        else:
            return 0
