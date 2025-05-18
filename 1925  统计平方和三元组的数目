class Solution:
    def countTriples(self, n: int) -> int:
        a = [i**2 for i in range(1, n + 1)]
        cnt = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if a[i] + a[j] == a[k]:
                        cnt += 1
        return cnt * 2
