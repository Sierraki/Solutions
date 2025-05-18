class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        dis = prices
        dis2 = [i for i in prices]
        top = 0
        dow = 1
        n = len(dis2)
        while top < n:
            dow = top + 1
            while dow < n:
                if dis[dow] <= prices[top]:
                    dis[top] = prices[dow]
                    break
                dow += 1
            else:
                dis[top] = 0
            top += 1
        l2 = [dis2[i] - dis[i] for i in range(n)]
        return l2
