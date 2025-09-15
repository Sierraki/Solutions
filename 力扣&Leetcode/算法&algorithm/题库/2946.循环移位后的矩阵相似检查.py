class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        def left(arr, k):
            n = len(arr)
            k = k % n
            return arr[k:] + arr[:k]

        def right(arr, k):
            n = len(arr)
            k = k % n
            return arr[-k:] + arr[:-k]

        for idx, i in enumerate(mat):
            if idx % 2 == 0:
                if mat[idx] != left(i, k):
                    return False
            else:
                if mat[idx] != right(i, k):
                    return False
        return True
