class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        n = len(sensor1)

        def fun(tar, test):
            for i in range(n):
                p1 = test[:i]
                p2 = test[i]
                p3 = test[i + 1 :]
                res = p1 + p3
                if res == tar[:-1] and p2 != tar[-1]:
                    return True
            return False

        if fun(sensor1, sensor2) == fun(sensor2, sensor1):
            return -1
        elif fun(sensor1, sensor2):
            return 1
        return 2
