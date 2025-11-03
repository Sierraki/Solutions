class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        tar = max(vat)
        if tar == 0:
            return 0
        res = float("inf")
        for save in range(1, tar + 1):
            ans = 0
            for i in range(len(vat)):
                if bucket[i] * save < vat[i]:
                    ans += ceil(vat[i] / save) - bucket[i]
            res = min(res, ans + save)
        return res
