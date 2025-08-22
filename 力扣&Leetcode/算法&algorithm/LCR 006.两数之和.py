class Solution(object):
    def twoSum(self, numbers, target):
        ans = -1
        check = Counter()
        for idx, i in enumerate(numbers):
            tar = target - i
            if tar not in check:
                check[tar] += idx
            if i in check:
                ans = [check[i], idx]
        return ans
