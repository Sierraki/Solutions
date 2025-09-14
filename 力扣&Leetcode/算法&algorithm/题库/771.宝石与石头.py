class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = [i for i in stones if i in jewels]
        return len(cnt)
