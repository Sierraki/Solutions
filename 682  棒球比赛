class Solution:
    def calPoints(self, operations: List[str]) -> int:

        cnt = operations.count("C")
        left = 0
        n = 0
        while n < cnt:
            if operations[left] == "C":
                if left > 0:
                    del operations[left - 1]
                del operations[left - 1]
                left -= 1
                n += 1
            else:
                left += 1
        # print(operations)
        for i in range(len(operations)):
            if operations[i] == "D":
                operations[i] = 2 * int(operations[i - 1])
            if operations[i] == "+":
                operations[i] = int(operations[i - 1]) + int(operations[i - 2])
            else:
                operations[i] = int(operations[i])
        return sum(operations)
