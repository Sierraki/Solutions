class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]
    ) -> List[int]:
        a = []
        n2 = len(arr2)
        n3 = len(arr3)
        for i in arr1:
            lc2 = bisect.bisect_left(arr2, i)
            lc3 = bisect.bisect_left(arr3, i)
            if lc2 < n2 and lc3 < n3:
                if i == arr2[lc2] == arr3[lc3]:
                    a.append(i)
        return a
