class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res = []
        swap = False
        if income > brackets[0][0]:
            for i in range(len(brackets)):
                if swap:
                    break
                if i == 0:
                    res.append([brackets[0][0], brackets[0][1]])
                else:
                    if income >= brackets[i][0]:
                        ans = [brackets[i][0] - brackets[i - 1][0], brackets[i][1]]
                    else:
                        ans = [income - brackets[i - 1][0], brackets[i][1]]
                        swap = True
                    res.append(ans)
        else:
            res.append([income, brackets[0][1]])
        ans = 0
        for i in res:
            ans += i[0] * i[1] / 100
        return ans
