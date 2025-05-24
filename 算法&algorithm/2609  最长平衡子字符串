class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        left = 0
        a = []
        b = []
        for idx, i in enumerate(s):
            if idx == len(s) - 1:
                if s[idx - 1] != i:
                    a.append(1)
                else:
                    a.append(idx - left + 1)
                if i == "1":
                    b.append(False)
                else:
                    b.append(True)
            elif i == s[left] and s[idx + 1] != i:
                if i == "1":
                    b.append(False)
                else:
                    b.append(True)
                a.append(idx - left + 1)
                left = idx + 1
        print(a, b)
        mx = 0
        n = len(a)
        for i in range(n - 1):
            if b[i] == True and b[i + 1] == False:
                mx = max(min(a[i], a[i + 1]) * 2, mx)
        print(mx)
        return mx
