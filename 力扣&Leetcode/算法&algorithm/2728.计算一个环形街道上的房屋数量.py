# Definition for a street.
# class Street:
#     def openDoor(self):
#         pass
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
#     def moveLeft(self):
#         pass
class Solution:
    def houseCount(self, street: Optional["Street"], k: int) -> int:
        while k > 0:
            if street.isDoorOpen() == False:
                street.openDoor()
            street.moveRight()
            k -= 1
        cnt = 0
        while street.isDoorOpen() == True:
            cnt += 1
            street.closeDoor()
            street.moveRight()
        return cnt
