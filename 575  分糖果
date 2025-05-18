class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = int(len(candyType) / 2)
        list1 = sorted(list(set(candyType)))
        cnt = 0
        for i in list1:
            if n > 0:
                cnt += 1
                n -= 1
            else:
                break
        return cnt
