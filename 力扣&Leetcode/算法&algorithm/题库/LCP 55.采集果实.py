class Solution:
    def getMinimumTime(
        self, time: List[int], fruits: List[List[int]], limit: int
    ) -> int:
        ans = 0
        for i, j in fruits:
            if j % limit == 0:
                tar = j // limit
            else:
                tar = j // limit + 1
            ans += time[i] * tar
        return ans
