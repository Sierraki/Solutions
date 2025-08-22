class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l, r = 0, len(mat[0]) - 1
        ans = 0
        for i in mat:
            ans += i[l] + i[r]
            l += 1
            r -= 1
        if len(mat) % 2 == 1:
            ans -= mat[len(mat) // 2][len(mat) // 2]
        return ans
