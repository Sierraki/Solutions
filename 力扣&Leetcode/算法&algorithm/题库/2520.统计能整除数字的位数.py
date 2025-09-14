class Solution:
    def countDigits(self, num: int) -> int:
        check = [int(i) for i in str(num)]
        cnt = 0
        for i in check:
            if num % i == 0:
                cnt += 1
        return cnt
