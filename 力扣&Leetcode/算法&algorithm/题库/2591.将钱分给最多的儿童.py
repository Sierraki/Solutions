class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        else:
            res = money - children
            cnt = res // 7
            if cnt >= children:
                cnt = children
                moneyleft = res - cnt * 7
                kidsleft = 0
            else:
                moneyleft = res - cnt * 7
                kidsleft = children - cnt
            if moneyleft == 3 and kidsleft == 1:
                ans = cnt - 1
            elif moneyleft > 0 and kidsleft == 0:
                ans = cnt - 1
            else:
                ans = cnt
        return ans
