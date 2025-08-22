class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        tar = len(bits) - 1
        pin = 0
        if len(bits) == 1 and bits[0] == 0:
            return True
        while pin < tar + 1:
            if bits[pin] == 1:
                pin += 2
            else:
                pin += 1
            if pin == tar:
                return True
            elif pin > tar:
                return False
