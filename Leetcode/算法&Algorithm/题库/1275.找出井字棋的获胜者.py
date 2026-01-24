class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        pos = [[0] * 3 for _ in range(3)]

        def col(tar=int) -> bool:
            cnt = set()
            for i in range(3):
                cnt.add(pos[i][tar])
            if len(cnt) == 1 and list(cnt)[0] != 0:
                return True
            return False

        def row(tar=int) -> bool:
            cnt = set(pos[tar])
            if len(cnt) == 1 and list(cnt)[0] != 0:
                return True
            return False

        def dig(tar=list) -> bool:
            x = tar[0]
            y = tar[1]
            if [x, y] in [[0, 0], [1, 1], [2, 2]]:
                if pos[0][0] == pos[1][1] == pos[2][2] and pos[2][2] != 0:
                    return True
            if [x, y] in [[0, 2], [1, 1], [2, 0]]:
                if pos[0][2] == pos[1][1] == pos[2][0] and pos[2][0] != 0:
                    return True
            return False

        for i in range(len(moves)):
            tar = moves[i]
            if i % 2 == 1:
                pos[tar[0]][tar[1]] = 1
            else:
                pos[tar[0]][tar[1]] = -1

            if col(tar[1]) == True or dig(tar) == True or row(tar[0]) == True:
                if i % 2 == 0:
                    return "A"
                else:
                    return "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"
