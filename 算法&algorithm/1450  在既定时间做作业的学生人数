class Solution:
    def busyStudent(
        self, startTime: List[int], endTime: List[int], queryTime: int
    ) -> int:
        list1 = []
        left = 0
        for right in endTime:
            list1.append([startTime[left], right])
            left += 1
        cnt = 0
        for i in list1:
            if queryTime >= i[0] and queryTime <= i[-1]:
                cnt += 1
        return cnt
