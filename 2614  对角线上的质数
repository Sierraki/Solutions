class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        l = 0
        a = []
        r = len(nums[0]) - 1
        for i in nums:
            a.append(i[l])
            l += 1
            a.append(i[r])
            r -= 1
        a.sort(reverse=True)
        for i in a:
            s = True
            if i == 1:
                continue
            else:
                for j in range(2, i):
                    if i % j == 0:
                        s = False
            if s == True:
                return i
                break
        else:
            return 0
