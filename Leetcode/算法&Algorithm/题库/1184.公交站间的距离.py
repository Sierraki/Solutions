class Solution:
    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        res1 = [start, destination]
        s = min(res1)
        e = max(res1)
        res = distance[s:e]
        return min(sum(res), sum(distance) - sum(res))
