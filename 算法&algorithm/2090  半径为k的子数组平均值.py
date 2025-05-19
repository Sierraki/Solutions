class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if 2 * k + 1 > n:
            return [-1 for i in range(n)]
        else:

            avg = int(sum(nums[: 2 * k + 1]) / (2 * k + 1))
            summ = sum(nums[: 2 * k + 1])
            a = [-1 for i in range(k)]  # -1-1-1-1-1-1
            com = []
            com = com + a
            com.append(avg)

            for i in range(k + 1, n - k):
                # return(i - k - 1, i, i + k)
                summ = summ + nums[i + k] - nums[i - k - 1]
                avg = int(summ / (2 * k + 1))

                com.append(avg)

            for i in range(k):
                com.append(-1)
            return com
