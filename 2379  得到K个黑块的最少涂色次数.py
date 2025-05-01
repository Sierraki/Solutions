class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)  # 10

        bcnt = 0

        for i in range(k):
            if blocks[i] == "B":
                bcnt += 1

        cur = bcnt
        big = cur

        for i in range(k, n):
            if blocks[i] == "B":
                cur += 1
            if blocks[i - k] == "B":
                cur -= 1
            if cur > big:
                big = cur

        return(k - big)
