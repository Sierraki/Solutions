class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def fun(res) -> bool:
            if len(res) > 1:
                for i in range(1, len(res)):
                    if ord(res[i]) - ord(res[i - 1]) < 0:
                        return False
            return True

        res = list(zip(*strs))
        cnt = 0
        for i in res:
            if not fun(i):
                cnt += 1
        return cnt
