class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        def ex(x=int) -> list:
            # 左边是新增的，右边的换完剩下的空瓶
            if x < numExchange:
                return [0, x]
            else:
                return [x // numExchange, x % numExchange]

        ans = numBottles
        while numBottles >= numExchange:
            res = ex(numBottles)
            numBottles = res[0] + res[1]
            ans += res[0]
        return ans
