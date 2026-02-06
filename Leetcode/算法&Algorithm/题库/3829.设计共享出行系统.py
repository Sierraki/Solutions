class RideSharingSystem:

    def __init__(self):
        self.driver = deque([])
        self.riders = {}

    def addRider(self, riderId: int) -> None:
        self.riders[riderId] = True

    def addDriver(self, driverId: int) -> None:
        self.driver.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if self.driver and self.riders:
            rider_id = next(iter(self.riders))
            del self.riders[rider_id]
            return [self.driver.popleft(), rider_id]
        return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.riders:
            del self.riders[riderId]


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)
