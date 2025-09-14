class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        # print(players)
        trainers.sort()
        cnt = 0
        for i in trainers:
            if players == []:
                break
            lc = bisect.bisect_left(players, i)
            # print(i, lc)
            if lc - 1 >= 0 and players[lc - 1] <= i:
                cnt += 1
                del players[lc - 1]
            elif lc < len(players) and players[lc] <= i:
                cnt += 1
                del players[lc]
        return cnt
