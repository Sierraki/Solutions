class Solution:
    def maximum69Number(self, num: int) -> int:
        a = [i for i in str(num)]
        cnt = 0
        for idx, i in enumerate(a):
            if i == "6" and cnt < 1:
                a[idx] = "9"
                cnt += 1
                break
        res = int("".join(a))
        return res
