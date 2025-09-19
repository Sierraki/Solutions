class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        res = deque([])
        word = deque(word)
        while word:
            if (not res or word[0] == res[-1]) and len(res) < 9:
                cur = word.popleft()
                res.append(cur)
            elif word[0] != res[-1] or len(res) == 9:
                n = len(res)
                ans += f"{n}{res[-1]}"
                res.clear()
        n = len(res)
        ans += f"{n}{res[-1]}"
        return ans
