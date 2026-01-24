class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        del salary[0]
        salary.pop()
        return sum(salary) / len(salary)
