class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        res = (-sum(aliceSizes) + sum(bobSizes)) // 2
        b = Counter()
        for idx, i in enumerate(bobSizes):
            b[i] = idx
        for i in aliceSizes:
            tar = res + i
            if tar in b:
                return [i, tar]
