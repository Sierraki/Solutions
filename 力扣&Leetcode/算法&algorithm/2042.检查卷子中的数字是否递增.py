class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        res = [int(i) for i in s.split() if i.isdigit()]
        for i in range(1, len(res)):
            if res[i - 1] >= res[i]:
                return False
        return True
