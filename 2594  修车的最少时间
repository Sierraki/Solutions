class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # check
        def check(t: int) -> bool:
            cnt = 0
            for i in ranks:
                cnt += floor(sqrt(t // i))#math
            return cnt >= cars

        # search left
        left, right = 0, min(ranks) * cars * cars
        while left < right:
            mid = (left + right) // 2
            if check(mid) == True:
                right = mid
            else:
                left = mid + 1
        return right
