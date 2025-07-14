class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnt = Counter(deck)
        mi = min(cnt.values())
        n = 1
        while n >= 1:
            if n > mi:
                return False
            n += 1
            for j in cnt.values():
                if j % n != 0:
                    break
            else:
                return True
