class Solution:
    def maxDistance(self, words: List[str]) -> int:

        if len(words) == 1:
            return 0
        elif len(words) == 2:
            if words[0] != words[1]:
                return 2
            else:
                return 0
        else:
            if words[0] != words[-1]:
                return len(words)
            ans = 0
            for i in range(1, len(words) - 1):
                if words[i] != words[0]:
                    ans = max(ans, i + 1)
                if words[i] != words[-1]:
                    ans = max(ans, len(words) - i)
        return ans
