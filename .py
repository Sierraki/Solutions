class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            for i in range(n):
                if n == 2**i:
                    return True
                    break
                elif 2**i > n:
                    return False
                    break


eg = Solution()
print(eg.isPowerOfTwo(1))  # true
print(eg.isPowerOfTwo(16))  # true
print(eg.isPowerOfTwo(13))  # false
