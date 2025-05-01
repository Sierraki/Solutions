class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
            arr2.sort()

            cnt = 0
            s = True

            for i in arr1:

                for j in arr2:
                    if abs(i - j) <= d:
                        s = False
                        break
                if s == True:
                    cnt += 1

                s = True

            return(cnt)
