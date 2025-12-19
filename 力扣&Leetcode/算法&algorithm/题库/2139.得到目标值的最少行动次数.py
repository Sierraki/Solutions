class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cnt = 0
        while target > 1:
            if target % 2 == 0:
                if maxDoubles > 0:
                    maxDoubles -= 1
                    target //= 2
                else:
                    target -= 1
                cnt += 1
            else:
                if maxDoubles > 0:
                    target -= 1
                    cnt += 1
                elif maxDoubles == 0:
                    cnt += target
                    return cnt - 1
        return cnt
