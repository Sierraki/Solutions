class Solution:
    def reverseMessage(self, message: str) -> str:
        res = [i for i in message.split()]
        res = res[::-1]
        for i in range(len(res) - 1, 0, -1):
            res.insert(i, " ")
        return "".join(res)
