class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        cnt = Counter(s)
        a = []
        for i, j in cnt.items():
            a.append([i, j])
        a.sort(key=lambda x: x[1])
        # print(a)
        diff = len(cnt) - k
        # print(diff)
        if diff <= 0:
            return 0
        else:
            cur = 0
            for i in range(diff):
                cur += a[i][1]
            return cur
