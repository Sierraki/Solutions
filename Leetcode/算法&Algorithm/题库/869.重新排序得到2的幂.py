class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        tar = len(str(n))
        cnt2 = Counter(str(n))
        for i in range(31623):
            if len(str(2**i)) == tar:
                cnt1 = Counter(str(2**i))
                if cnt1 == cnt2:
                    return True
            elif len(str(2**i)) > tar:
                return False
        return False
