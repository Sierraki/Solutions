class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        dif = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if not (arr[i - 1] + dif == arr[i]):
                return False
        return True
