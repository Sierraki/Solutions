class Solution:
    def supplyWagon(self, supplies: List[int]) -> List[int]:
        def fun(supplies: list):
            mi = float("inf")
            for i in range(len(supplies) - 1):
                if supplies[i] + supplies[i + 1] < mi:
                    mi = supplies[i] + supplies[i + 1]
                    l = i
            supplies[l] += supplies[l + 1]
            del supplies[l + 1]
            return supplies

        n = len(supplies)
        while len(supplies) > n // 2:
            supplies = fun(supplies)
        return supplies
