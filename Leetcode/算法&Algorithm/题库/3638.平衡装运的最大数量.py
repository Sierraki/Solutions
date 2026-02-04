class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        pin = 1
        cnt = 0
        while pin < len(weight):
            if weight[pin - 1] > weight[pin]:
                cnt += 1
                pin += 2
            else:
                pin += 1
        return cnt
