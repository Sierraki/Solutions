from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                arr[i] = 1
            else:
                arr[i] = 0
        st = False
        left = 0
        cur = sum(arr[left:3])
        if cur == 3:
            st = True
        else:
            for i in range(3, len(arr)):
                cur += arr[i]
                cur -= arr[i - 3]
                if cur >= 3:
                    st = True
                    break
        return st
