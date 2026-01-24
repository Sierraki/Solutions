class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        pin = 0
        cnt = 0
        while pin < m + n and B:
            if A[pin] >= B[0]:
                A.insert(pin, B[0])
                del B[0]
                del A[-1]
                cnt += 1
            else:
                pin += 1
        pin = 0
        for i in range(cnt + m, len(A)):
            A[i] = B[pin]
            pin += 1
