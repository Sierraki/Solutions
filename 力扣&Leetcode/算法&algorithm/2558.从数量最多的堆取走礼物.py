class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k > 0:
            k -= 1
            gifts.sort()
            gifts[-1] = floor(sqrt(gifts[-1]))
        return sum(gifts)
