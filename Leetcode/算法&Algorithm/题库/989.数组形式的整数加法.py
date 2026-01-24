class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        if len(num) < len(str(k)):
            res = num.copy()
            num = [int(i) for i in str(k)]
            k = res
        else:
            k = [int(i) for i in str(k)]
        pin = -1
        while -pin <= len(k):
            num[pin] += int(k[pin])
            pin -= 1
        # 最后处理
        for i in range(len(num) - 1, 0, -1):
            if num[i] >= 10:
                num[i - 1] += num[i] // 10
                num[i] = num[i] % 10
        if num[0] >= 10:
            num.insert(0, num[0] // 10)
            num[1] = num[1] % 10
        return num
