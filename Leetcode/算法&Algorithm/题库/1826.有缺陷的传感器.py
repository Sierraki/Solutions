class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        n = len(sensor1)

        def fun(tar, test):
            for i in range(n):
                if test[:i] + test[i + 1 :] == tar[:-1] and test[i] != tar[-1]:
                    return True
            return False

        if fun(sensor1, sensor2) == fun(sensor2, sensor1):
            return -1
        elif fun(sensor1, sensor2):
            return 1
        return 2
