class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        code += code

        if k > 0:
            init = sum(code[:k])
            for i in range(k, k + n):
                init += code[i] - code[i - k]
                code[i - k] = init
            return(code[:n])

        elif k < 0:
            init = sum(code[n + k : n])
            code[0] = init
            for i in range(n, 2 * n):
                init += code[i] - code[i + k]
                code[i - n + 1] = init
            return(code[:n])

        else:
            return([0 for i in range(n)])

                