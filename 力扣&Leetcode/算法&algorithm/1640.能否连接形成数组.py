class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        cnt = {i: idx for idx, i in enumerate(arr)}
        for i in pieces:
            if len(i) > 1:
                for j in range(1, len(i)):
                    if (
                        (i[j] not in cnt)
                        or (i[j - 1] not in cnt)
                        or cnt[i[j - 1]] + 1 != cnt[i[j]]
                    ):
                        return False
            else:
                if i[0] not in cnt:
                    return False
        return True
