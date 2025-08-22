class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for i in logs:
            if i[-1] == "/" and len(i) >= 3 or i == "../":
                if i == "../":
                    if res > 0:
                        res -= 1
                    else:
                        res = 0
                else:
                    res += 1
            elif i == "./":
                res += 0
            elif i[-1] == "/" and len(i) == 2:
                res += 1
        return res
