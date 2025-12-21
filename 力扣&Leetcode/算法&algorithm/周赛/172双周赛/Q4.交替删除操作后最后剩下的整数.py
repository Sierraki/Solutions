class Solution:
    def lastInteger(self, n: int) -> int:
        # 第一次左步长2
        # 第一次右4
        # 第二次左8
        # pin第一次移动2
        # 第二次8
        pin = 1
        step = 1
        cnt = n
        while cnt > 1:
            # -->
            cnt = (cnt + 1) // 2
            step *= 2
            if cnt == 1:
                return pin
            # <--
            if cnt % 2 == 0:
                pin += step
            cnt = (cnt + 1) // 2
            step *= 2
            if cnt == 1:
                return pin
        return pin
