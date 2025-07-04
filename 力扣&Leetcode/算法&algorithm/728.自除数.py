class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check(k: int) -> bool:
            res = []
            for i in str(k):
                if i == "0":
                    return False
                res.append(int(i))
            for i in res:
                if k % i != 0:
                    return False
            return True

        res = []
        for i in range(left, right + 1):
            if check(i):
                res.append(i)
        return res
