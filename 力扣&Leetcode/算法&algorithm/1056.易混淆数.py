class Solution:
    def confusingNumber(self, n: int) -> bool:
        check = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        nums = []
        for i in range(len(str(n)) - 1, -1, -1):
            if str(n)[i] not in check:
                return False
            nums.append(str(n)[i])
        res = "".join([check[i] for i in nums])
        return int(res) != n
