class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        mx = ans = 0
        n = len(word)
        for i in range(n - 1, len(sequence)):
            ans = 0
            pin = i
            while pin >= 0:
                if (sequence[pin - n + 1 : pin + 1]) == word:
                    ans += 1
                    mx = max(mx, ans)
                    pin -= n
                else:
                    break
        return mx
